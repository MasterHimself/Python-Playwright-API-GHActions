
from __future__ import annotations

import pytest


@pytest.mark.api
def test_get_all_categories_returns_response(categories_api) -> None:
    resp = categories_api.get_all_categories()
    assert resp.status_code < 500


@pytest.mark.api
def test_get_all_categories_has_body(categories_api) -> None:
    resp = categories_api.get_all_categories()
    assert resp.status_code < 500
    assert resp.text is not None

