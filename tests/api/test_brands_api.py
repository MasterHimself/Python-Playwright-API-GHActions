
from __future__ import annotations

import pytest


@pytest.mark.api
def test_get_all_brands(brands_api) -> None:
    resp = brands_api.get_all_brands()
    assert resp.status_code == 200


@pytest.mark.api
def test_get_all_brands_has_json_like_payload(brands_api) -> None:
    resp = brands_api.get_all_brands()
    assert resp.status_code == 200
    assert resp.text is not None

