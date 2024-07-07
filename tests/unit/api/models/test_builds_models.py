import pytest
from uuid import UUID
from pydantic import ValidationError

from app.api.models.builds import GenerateBuildRequest


def test_build_request_valid() -> None:
    data = {
        "build_name": "test-build",
        "switch_id": "02c80c98-069d-4771-bb00-802962186574",
        "kit_id": "051db3a8-9ba9-42c9-a58e-b2acc11ffd58",
        "keycap_id": "0208b85c-2b57-4a5a-8e0f-8993bfe9c20c",
        "lubricant_id": "56121e0f-cc68-4d54-a7fd-a28dd19fefd4"
    }

    build_request = GenerateBuildRequest(**data)

    assert build_request.build_name == "test-build"
    assert build_request.switch_id == UUID("02c80c98-069d-4771-bb00-802962186574")
    assert build_request.kit_id == UUID("051db3a8-9ba9-42c9-a58e-b2acc11ffd58")
    assert build_request.keycap_id == UUID("0208b85c-2b57-4a5a-8e0f-8993bfe9c20c")
    assert build_request.lubricant_id == UUID("56121e0f-cc68-4d54-a7fd-a28dd19fefd4")


def test_build_request_missing_information() -> None:
    data = {
        "build_name": "test-build",
        "switch_id": "02c80c98-069d-4771-bb00-802962186574"
    }

    with pytest.raises(ValidationError):
        GenerateBuildRequest(**data)


def test_build_request_empty_build() -> None:
    data = {
        "build_name": "",
        "switch_id": "",
        "kit_id": "",
        "keycap_id": "",
        "lubricant_id": ""
    }

    with pytest.raises(ValidationError):
        GenerateBuildRequest(**data)
