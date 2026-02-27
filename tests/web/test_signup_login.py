import pytest
from pages.signup_login_page import SignupLoginPage

@pytest.mark.web
def test_signup_login_page_loads(page, config):
    login_page = SignupLoginPage(page)
    login_page.navigate(config.get_base_url() + "/login")
    assert login_page.is_login_form_visible()


@pytest.mark.web
def test_invalid_login(page, config):
    login_page = SignupLoginPage(page)
    login_page.navigate(config.get_base_url() + "/login")
    login_page.login("fake@example.com", "wrongpass")
    assert login_page.is_login_error_visible()

