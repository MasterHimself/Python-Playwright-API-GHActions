import pytest
from pages.contact_page import ContactPage

@pytest.mark.web
def test_contact_form_presence(page, config):
    contact = ContactPage(page)
    contact.navigate(config.get_base_url() + "/contact_us")
    assert contact.is_form_displayed()


@pytest.mark.web
def test_submit_contact_form(page, config, tmp_path) -> None:
    contact = ContactPage(page)
    contact.navigate(config.get_base_url() + "/contact_us")
    upload_file = tmp_path / "upload.txt"
    upload_file.write_text("hello", encoding="utf-8")

    contact.submit_form_with_data(
        "John",
        "john@example.com",
        "Subject",
        "Message",
        file_path=str(upload_file),
    )

    page.wait_for_selector("div.status.alert", state="attached", timeout=15000)
    assert page.locator("div.status.alert").count() > 0

