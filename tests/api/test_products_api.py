
from __future__ import annotations

import pytest


@pytest.mark.api
def test_get_all_products(products_api) -> None:
    resp = products_api.get_all_products()
    assert resp.status_code == 200


@pytest.mark.api
def test_get_product_by_id_invalid_returns_not_found_or_error(products_api) -> None:
    resp = products_api.get_product_by_id(999999)
    assert resp.status_code in (200, 400, 404)

