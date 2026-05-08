"""CostEstimate + estimate_scene_cost rollup."""

from __future__ import annotations

import pytest

from falaw import (
    Beat,
    Character,
    CostEstimate,
    CostRollup,
    Environment,
    ModelRecord,
    Scene,
    Voice,
    estimate_call_cost,
    estimate_scene_cost,
    make_beat,
    make_shot,
)
from falaw import registry


@pytest.fixture(autouse=True)
def _isolated(tmp_path, monkeypatch):
    monkeypatch.setenv("FALAW_DATA_DIR", str(tmp_path))
    monkeypatch.setenv("FALAW_CACHE_DIR", str(tmp_path / "cache"))


def test_cost_estimate_per_call():
    record = ModelRecord(
        id="x",
        category="image",
        cost_estimate=CostEstimate(kind="per_call", amount=0.05),
    )
    assert estimate_call_cost(record) == pytest.approx(0.05)
    assert estimate_call_cost(record, count=3) == pytest.approx(0.15)


def test_cost_estimate_per_second():
    record = ModelRecord(
        id="x",
        category="text_to_video",
        cost_estimate=CostEstimate(kind="per_second", amount=0.10),
    )
    assert estimate_call_cost(record, seconds=12.0) == pytest.approx(1.20)


def test_cost_estimate_per_megapixel_uses_default_when_missing():
    record = ModelRecord(
        id="x",
        category="image",
        cost_estimate=CostEstimate(kind="per_megapixel", amount=0.10),
    )
    # Default 0.6 MP if megapixels not supplied.
    assert estimate_call_cost(record) == pytest.approx(0.06)
    assert estimate_call_cost(record, megapixels=2.0) == pytest.approx(0.20)


def test_estimate_call_cost_returns_none_when_no_estimate():
    """Distinguish 'no estimate' from 'free'."""
    record = ModelRecord(id="x", category="image")
    assert estimate_call_cost(record) is None


def test_estimate_scene_cost_aggregates_per_line(monkeypatch):
    """Estimate a scene with one shot + two beats and assert the rollup math."""

    # Override pick_model so test is deterministic and doesn't depend on
    # whatever costs are wired into the live catalog.
    fake_records = {
        "image": ModelRecord(
            id="img-fast",
            category="image",
            quality_tier="balanced",
            cost_estimate=CostEstimate(kind="per_image", amount=0.04),
        ),
        "tts": ModelRecord(
            id="tts-balanced",
            category="tts",
            quality_tier="balanced",
            cost_estimate=CostEstimate(kind="per_second", amount=0.02),
        ),
        "avatar": ModelRecord(
            id="ai-avatar",
            category="avatar",
            quality_tier="high",
            cost_estimate=CostEstimate(kind="per_second", amount=0.10),
        ),
    }

    import falaw.cost as cost_mod

    def fake_pick_model(*, category, quality_tier="balanced"):
        return fake_records[category]

    monkeypatch.setattr(cost_mod, "pick_model", fake_pick_model)

    sarah = Character(
        name="Sarah",
        reference_image_url="http://x/sarah.png",
        voice=Voice(name="Sarah", voice_id="v1"),
    )
    diner = Environment(name="diner", description="1950s diner")
    shot = make_shot(
        "two-shot at the booth", framing="medium", environment="diner",
        characters=("Sarah",), index=0,
    )
    scene = Scene(
        title="t",
        characters=(sarah,),
        environments=(diner,),
        shots=(shot,),
        beats=(
            make_beat("Sarah", "Why are you here?", shot_id=shot.id, index=0),
            make_beat("Sarah", "I came to see you.", shot_id=shot.id, index=1),
        ),
    )

    rollup = estimate_scene_cost(scene)
    assert isinstance(rollup, CostRollup)

    # Expected: 1 image ($0.04) + per-beat (tts + avatar) at 0.4s/word.
    # Beat 1 "Why are you here?" — 4 words → 1.6s.
    # Beat 2 "I came to see you." — 5 words → 2.0s.
    # Beat cost: secs × ($0.02 tts + $0.10 avatar) = secs × 0.12
    expected = 0.04 + 1.6 * 0.12 + 2.0 * 0.12
    assert rollup.total_amount == pytest.approx(expected, abs=0.01)
    by_kind = rollup.by_kind()
    assert "shot.image" in by_kind
    assert "beat.tts" in by_kind
    assert "beat.avatar" in by_kind


def test_estimate_scene_cost_skipped_lists_unpriced_models(monkeypatch):
    """When no cost_estimate is set, the model is reported in 'skipped'."""
    import falaw.cost as cost_mod

    fake_records = {
        "image": ModelRecord(id="img-no-cost", category="image"),  # no estimate
        "tts": ModelRecord(
            id="tts",
            category="tts",
            cost_estimate=CostEstimate(kind="per_second", amount=0.01),
        ),
        "avatar": ModelRecord(
            id="avatar",
            category="avatar",
            cost_estimate=CostEstimate(kind="per_second", amount=0.05),
        ),
    }
    monkeypatch.setattr(
        cost_mod, "pick_model",
        lambda *, category, quality_tier="balanced": fake_records[category],
    )

    sarah = Character(
        name="Sarah",
        reference_image_url="http://x/s.png",
        voice=Voice(name="Sarah", voice_id="v"),
    )
    shot = make_shot("a", index=0)
    scene = Scene(title="t", characters=(sarah,), shots=(shot,), beats=())

    rollup = estimate_scene_cost(scene)
    assert any("img-no-cost" in s for s in rollup.skipped)
    # Total should not include the unpriced shot.
    assert rollup.total_amount == 0.0


def test_estimate_scene_cost_includes_video_when_shots_as_video(monkeypatch):
    import falaw.cost as cost_mod

    fake_records = {
        "image": ModelRecord(
            id="i",
            category="image",
            cost_estimate=CostEstimate(kind="per_image", amount=0.04),
        ),
        "image_to_video": ModelRecord(
            id="i2v",
            category="image_to_video",
            cost_estimate=CostEstimate(kind="per_second", amount=0.50),
        ),
    }
    monkeypatch.setattr(
        cost_mod, "pick_model",
        lambda *, category, quality_tier="balanced": fake_records[category],
    )

    shot = make_shot("a", index=0)

    # The Shot dataclass doesn't carry duration; we approximate with 0
    # for the price test (per_second × 0 = 0). Scene-shot duration comes
    # from the renderer's per-shot run, not from Shot itself, so the
    # scene-rollup will price the i2v line at 0 here. The test still
    # asserts the line APPEARS — correctness of duration is the
    # caller's job (passing seconds= when calling estimate_call_cost).
    scene = Scene(title="t", shots=(shot,))
    rollup = estimate_scene_cost(scene, shots_as_video=True)
    kinds = {ln.kind for ln in rollup.lines}
    assert "shot.image" in kinds
    assert "shot.video" in kinds


def test_cost_rollup_by_kind_sums_correctly():
    rollup = CostRollup(
        total_amount=0.30,
        lines=(
            cost_line("shot.image", "s1", 0.04),
            cost_line("shot.image", "s2", 0.04),
            cost_line("beat.tts",   "b1", 0.10),
            cost_line("beat.avatar", "b1", 0.12),
        ),
    )
    by_kind = rollup.by_kind()
    assert by_kind["shot.image"] == pytest.approx(0.08)
    assert by_kind["beat.tts"] == pytest.approx(0.10)
    assert by_kind["beat.avatar"] == pytest.approx(0.12)


def cost_line(kind, item_id, amount):
    from falaw import CostLine

    return CostLine(
        kind=kind, item_id=item_id, model_id="m",
        amount=amount, currency="USD",
    )


# --- Regression: actively-used models have populated cost_estimate ----------


def test_priced_models_loaded_from_data_json():
    """Selected models in data/models.json must have a populated cost_estimate."""
    from falaw.registry import _load_models

    _load_models.cache_clear()
    models = _load_models()
    must_be_priced = {
        "fal-ai/flux/dev",
        "fal-ai/flux-pro/v1.1",
        "fal-ai/bytedance/omnihuman/v1.5",
        "fal-ai/minimax/hailuo-02/pro/image-to-video",
    }
    for mid in must_be_priced:
        assert mid in models, f"{mid} missing from models.json"
        assert models[mid].cost_estimate is not None, (
            f"{mid} has no cost_estimate populated — agents can't budget without it"
        )


def test_hailuo_uses_per_call_pricing():
    """Hailuo Pro is priced per-clip (fixed ~5.87s output), not per-second."""
    from falaw.registry import _load_models

    _load_models.cache_clear()
    hailuo = _load_models()["fal-ai/minimax/hailuo-02/pro/image-to-video"]
    assert hailuo.cost_estimate is not None
    assert hailuo.cost_estimate.kind == "per_call"
    cost = estimate_call_cost(hailuo)
    assert cost is not None and cost > 0


def test_omnihuman_per_second_pricing_matches_empirical():
    """OmniHuman cost matches the empirical observation: 8s ≈ $0.80."""
    from falaw.registry import _load_models

    _load_models.cache_clear()
    omni = _load_models()["fal-ai/bytedance/omnihuman/v1.5"]
    assert omni.cost_estimate is not None
    assert omni.cost_estimate.kind == "per_second"
    cost = estimate_call_cost(omni, seconds=8.0)
    assert cost is not None
    # Allow ±25% wiggle: this is ground for fluctuation in fal pricing.
    assert 0.6 < cost < 1.0
