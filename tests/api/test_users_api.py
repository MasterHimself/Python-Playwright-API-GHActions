
from __future__ import annotations

import pytest


@pytest.mark.api
def test_login_user_missing_fields_returns_error(users_api) -> None:
    resp = users_api.login_user({"password": "123"})
    if resp.status_code in (400, 404):
        return

    assert resp.status_code == 200
    body = resp.text.lower()
    try:
        payload = resp.json()
    except ValueError:
        payload = None

    if isinstance(payload, dict) and "responseCode" in payload:
        assert int(payload["responseCode"]) in (400, 404)
        return

    assert "missing" in body or "bad request" in body or "not found" in body


@pytest.mark.api
def test_create_user_missing_fields_returns_error(users_api) -> None:
    resp = users_api.create_user({"email": "qa@example.com"})
    if resp.status_code in (400, 404):
        return

    assert resp.status_code == 200
    body = resp.text.lower()
    try:
        payload = resp.json()
    except ValueError:
        payload = None

    if isinstance(payload, dict) and "responseCode" in payload:
        assert int(payload["responseCode"]) in (400, 404)
        return

    assert "missing" in body or "bad request" in body

