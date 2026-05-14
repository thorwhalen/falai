"""Tests for Plan ↔ dict serialization (``plan_to_dict`` / ``plan_from_dict``).

A :class:`falaw.Plan` is pure data; these functions give it a stable,
JSON-serializable wire shape so consumers (persistence layers, MCP transports,
plan-diff tools) all agree on it. The contract: round-trip is lossless and
JSON-clean.
"""

from __future__ import annotations

import json

import pytest

from falaw import (
    CallPlan,
    PLAN_DICT_SCHEMA,
    Plan,
    call_plan_from_dict,
    call_plan_to_dict,
    plan_from_dict,
    plan_to_dict,
)


def _sample_plan() -> Plan:
    """A two-step plan exercising every CallPlan field, including the awkward ones."""
    p1 = CallPlan(
        tool="generate_image",
        application="fal-ai/flux/dev",
        arguments={"prompt": "a tiger", "image_size": "landscape_4_3"},
        output_kind="image",
        estimated_cost_usd=0.025,
        cache_status="miss",
        metadata={"shot_id": "s01"},
    )
    p2 = CallPlan(
        tool="image_to_video",
        application="fal-ai/minimax/hailuo-02/pro/image-to-video",
        arguments={"image_url": "<from 0>"},
        output_kind="video",
        estimated_cost_usd=0.50,
        cache_status="unknown",
        expected_duration_s=(2.0, 8.0),
        metadata={},
    )
    return Plan(calls=(p1, p2))


def test_call_plan_round_trip_is_lossless():
    call = _sample_plan().calls[1]
    restored = call_plan_from_dict(call_plan_to_dict(call))
    assert restored == call
    # the tuple field survived the list detour intact
    assert restored.expected_duration_s == (2.0, 8.0)
    assert isinstance(restored.expected_duration_s, tuple)


def test_plan_round_trip_is_lossless():
    plan = _sample_plan()
    restored = plan_from_dict(plan_to_dict(plan))
    assert restored == plan


def test_plan_dict_is_json_serializable():
    plan = _sample_plan()
    blob = json.dumps(plan_to_dict(plan))  # must not raise
    restored = plan_from_dict(json.loads(blob))
    assert restored == plan


def test_plan_dict_carries_schema_tag():
    assert plan_to_dict(_sample_plan())["schema"] == PLAN_DICT_SCHEMA


def test_empty_plan_round_trips():
    assert plan_from_dict(plan_to_dict(Plan())) == Plan()


def test_plan_from_dict_tolerates_missing_schema():
    # hand-written plans without a schema tag are treated as v1
    d = plan_to_dict(_sample_plan())
    del d["schema"]
    assert plan_from_dict(d) == _sample_plan()


def test_plan_from_dict_rejects_unknown_schema():
    d = plan_to_dict(_sample_plan())
    d["schema"] = "falaw.plan/v999"
    with pytest.raises(ValueError, match="unknown schema"):
        plan_from_dict(d)


def test_deserialized_plan_owns_its_mutable_data():
    # arguments / metadata must be copies — mutating the source dict after
    # deserialization must not leak into the rebuilt CallPlan.
    src = call_plan_to_dict(_sample_plan().calls[0])
    restored = call_plan_from_dict(src)
    src["arguments"]["prompt"] = "MUTATED"
    src["metadata"]["shot_id"] = "MUTATED"
    assert restored.arguments["prompt"] == "a tiger"
    assert restored.metadata["shot_id"] == "s01"
