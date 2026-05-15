"""End-to-end Plan/Execute round-trip test.

Exercises the full Phase-1a contract:

1. Build a multi-step Plan (generate_image → image_to_video) without any
   API access.
2. Inspect the Plan: total_cost_usd, cache_hit_savings_usd, has_unknown_costs.
3. Execute via a stubbed fal_client.
4. Verify the resulting Artifacts are well-formed (URLs extracted,
   provenance set, costs propagated).
5. Re-execute and verify the cache short-circuits the second pass — and
   that re-planning shows cache_status='hit'.

This is the keystone test for Phase 1a: it's the first end-to-end proof
that an agent can build a multi-step render plan and drive it without
writing bash glue.
"""

from __future__ import annotations

import sys
import types
from pathlib import Path

import pytest


@pytest.fixture(autouse=True)
def _isolated(tmp_path, monkeypatch):
    monkeypatch.setenv("FALAW_DATA_DIR", str(tmp_path))
    monkeypatch.setenv("FALAW_CACHE_DIR", str(tmp_path / "cache"))
    from falaw.events import clear_subscribers
    from falaw.journal import _default_journal

    _default_journal.cache_clear()
    clear_subscribers()
    yield
    clear_subscribers()
    _default_journal.cache_clear()


def _patch_fal(monkeypatch):
    """Install a fal_client stub. Returns a list that grows with each call."""
    captured: list[dict] = []

    def subscribe(application, *, arguments, with_logs, on_queue_update):
        captured.append({"application": application, "arguments": dict(arguments)})
        if "image-to-video" in application or "hailuo" in application:
            return {
                "video": {
                    "url": "http://x/animated.mp4",
                    "duration": 8.0,
                    "content_type": "video/mp4",
                }
            }
        if "omnihuman" in application or "ai-avatar" in application:
            return {"video": {"url": "http://x/talk.mp4", "duration": 5.0,
                              "content_type": "video/mp4"}}
        if "flux-kontext" in application or "image_edit" in application:
            return {"images": [{"url": "http://x/edited.png",
                                "content_type": "image/png"}]}
        # Default: image generation.
        return {"images": [{"url": "http://x/img.png", "content_type": "image/png"}]}

    fake = types.SimpleNamespace(
        InProgress=type("IP", (), {"__init__": lambda s, logs: None}),
        subscribe=subscribe,
    )
    monkeypatch.setitem(sys.modules, "fal_client", fake)
    return captured


def test_two_step_render_plan_roundtrip(monkeypatch):
    """The keystone test: plan → inspect → execute → verify Artifacts."""
    captured = _patch_fal(monkeypatch)
    from falaw import (
        Plan,
        execute_plan,
        plan_generate_image,
        plan_image_to_video,
    )

    # 1. Build a plan WITHOUT any fal contact.
    p1 = plan_generate_image(
        prompt="bell tower in moonlight",
        quality="balanced",
        metadata={"shot_id": "s01", "step": "still"},
    )
    p2 = plan_image_to_video(
        # In real use, p2's image_url would be filled in after p1 executes,
        # or via a placeholder the orchestrator resolves. For this test we
        # use a literal URL to keep the planning step self-contained.
        # Reference the upstream plan_generate_image artifact via the
        # canonical placeholder syntax. The executor rewrites this to
        # artifacts[0].url just before the i2v call fires.
        image_url="<from 0>",
        duration_s=3.0,
        metadata={"shot_id": "s01", "step": "motion"},
    )
    plan = Plan(calls=(p1, p2))
    assert captured == [], "planning should not have made any API calls"

    # 2. Inspect — should report a positive cost from the populated estimates.
    assert plan.total_cost_usd > 0
    assert plan.cache_hit_savings_usd == 0  # nothing cached yet
    assert plan.has_unknown_costs is False, (
        f"both ops should have populated cost_estimate; plan: "
        f"{[(c.tool, c.application, c.estimated_cost_usd) for c in plan.calls]}"
    )

    # The cache_status should be 'miss' for both calls (they haven't run).
    assert all(c.cache_status == "miss" for c in plan.calls)

    # 3. Execute — should produce two Artifacts.
    artifacts = execute_plan(plan)
    assert len(artifacts) == 2

    img_artifact, video_artifact = artifacts
    assert img_artifact.kind == "image"
    assert img_artifact.url == "http://x/img.png"
    assert img_artifact.mime == "image/png"
    assert img_artifact.cost_usd is not None and img_artifact.cost_usd > 0

    assert video_artifact.kind == "video"
    assert video_artifact.url == "http://x/animated.mp4"
    assert video_artifact.duration_s == 8.0
    assert video_artifact.cost_usd is not None and video_artifact.cost_usd > 0

    # Provenance is set.
    assert img_artifact.provenance.was_generated_by.startswith("agent:fal@")
    assert img_artifact.provenance.activity == "create"

    # Captured exactly two fal calls.
    assert len(captured) == 2

    # 4. Re-execute — cache should short-circuit, no new fal calls.
    captured.clear()
    artifacts_again = execute_plan(plan)
    assert len(captured) == 0, "second execute should hit the cache"
    # Same content → same URLs → same Artifact asset_ids.
    assert artifacts_again[0].asset_id == img_artifact.asset_id
    assert artifacts_again[1].asset_id == video_artifact.asset_id

    # 5. Re-plan — now cache_status should report 'hit'.
    p1_after = plan_generate_image(
        prompt="bell tower in moonlight",
        quality="balanced",
        metadata={"shot_id": "s01", "step": "still"},
    )
    assert p1_after.cache_status == "hit", (
        "after a successful execute, re-planning the same call should report a cache hit"
    )

    # And the post-cache plan reports the savings:
    plan_after = Plan(calls=(p1_after,))
    assert plan_after.total_cost_usd == 0.0  # cache hit means no billable cost
    assert plan_after.cache_hit_savings_usd > 0


def test_dry_run_plan_does_not_call_fal(monkeypatch):
    """dry_run=True must not call fal under any circumstance."""
    captured = _patch_fal(monkeypatch)
    from falaw import Plan, execute_plan, plan_generate_image

    plan = Plan(calls=(plan_generate_image(prompt="x"),))
    artifacts = execute_plan(plan, dry_run=True)
    assert captured == []  # no API calls
    assert len(artifacts) == 1
    assert artifacts[0].url is None  # synthetic
    assert artifacts[0].kind == "image"


def test_plan_with_explicit_model_id_pins_application(monkeypatch):
    """plan_*(model_id=…) bypasses pick_model and pins the application field."""
    from falaw import plan_animate_face

    p = plan_animate_face(
        image_url="http://x/face.png",
        audio_url="http://x/voice.mp3",
        model_id="fal-ai/bytedance/omnihuman/v1.5",
        duration_s=8.0,
    )
    assert p.application == "fal-ai/bytedance/omnihuman/v1.5"
    # Cost estimate from the empirical $0.10/s * 8s = $0.80
    assert p.estimated_cost_usd == pytest.approx(0.80)


def test_plan_image_to_video_uses_per_call_cost_for_hailuo(monkeypatch):
    """Hailuo Pro is per_call ($0.50/clip) — duration_s shouldn't multiply cost."""
    from falaw import plan_image_to_video

    p = plan_image_to_video(
        image_url="http://x/img.png",
        model_id="fal-ai/minimax/hailuo-02/pro/image-to-video",
        duration_s=8.0,  # ignored for per_call pricing
    )
    assert p.estimated_cost_usd == pytest.approx(0.50)


def test_plan_text_to_speech_builds_tts_call():
    """plan_text_to_speech mirrors plan_lipsync's shape — tool, application,
    arguments, output_kind. Picks a TTS model by quality tier."""
    from falaw import plan_text_to_speech

    p = plan_text_to_speech(text="Hello world", quality="balanced")
    assert p.tool == "text_to_speech"
    assert p.output_kind == "audio"
    assert p.arguments["text"] == "Hello world"
    assert "voice" not in p.arguments  # omitted when not passed
    assert p.application  # some TTS model resolved


def test_plan_text_to_speech_threads_voice_and_extra():
    from falaw import plan_text_to_speech

    p = plan_text_to_speech(
        text="Salut",
        voice="fr-FR-female-1",
        extra={"stability": 0.5},
        metadata={"panel_id": "p01"},
    )
    assert p.arguments["text"] == "Salut"
    assert p.arguments["voice"] == "fr-FR-female-1"
    assert p.arguments["stability"] == 0.5
    assert p.metadata == {"panel_id": "p01"}


def test_plan_text_to_speech_pins_explicit_model_id():
    from falaw import plan_text_to_speech

    p = plan_text_to_speech(
        text="x",
        model_id="fal-ai/elevenlabs/tts/multilingual-v2",
    )
    assert p.application == "fal-ai/elevenlabs/tts/multilingual-v2"


def test_full_plan_with_metadata_threading(monkeypatch):
    """Metadata propagates from CallPlan to executed Artifact's
    producer_call_id-adjacent fields. (Today we attach it via the converter
    only when the orchestrator chooses; the plan carries the raw metadata.)"""
    _patch_fal(monkeypatch)
    from falaw import Plan, execute_plan, plan_generate_image

    p = plan_generate_image(
        prompt="x",
        metadata={"shot_id": "s01", "attributed_to": "user:thor"},
    )
    plan = Plan(calls=(p,))
    artifacts = execute_plan(plan)
    # Default converter reads attributed_to from metadata for provenance.
    assert artifacts[0].provenance.was_attributed_to == "user:thor"
