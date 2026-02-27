
from __future__ import annotations

import pytest


@pytest.mark.api
def test_search_product_success(search_api) -> None:
    resp = search_api.search_product("top")
    assert resp.status_code == 200


@pytest.mark.api
def test_search_product_empty_query_returns_error_or_empty(search_api) -> None:
    resp = search_api.search_product("")
    assert resp.status_code in (200, 400)

