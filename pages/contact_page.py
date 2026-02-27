from playwright.sync_api import Page

from pages.base_page import BasePage


class ContactPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.name_input = "//input[@placeholder='Name']"
        self.email_input = "//input[@placeholder='Email']"
        self.subject_input = "//input[@placeholder='Subject']"
        self.message_textarea = "//textarea[@placeholder='Your Message Here']"
        self.upload_input = "input[name='upload_file']"
        self.submit_btn = "//button[@type='submit']"
        self.success_message = "div.status.alert.alert-success"

    def fill_contact_form(self, name: str, email: str, subject: str, message: str) -> None:
        self.page.fill(self.name_input, name)
        self.page.fill(self.email_input, email)
        self.page.fill(self.subject_input, subject)
        self.page.fill(self.message_textarea, message)

    def submit_form(
        self,
        name: str = None,
        email: str = None,
        subject: str = None,
        message: str = None,
        file_path: str = None,
    ) -> None:
        if all([name, email, subject, message]):
            self.fill_contact_form(name, email, subject, message)
        if file_path:
            self.page.set_input_files(self.upload_input, file_path)
        self.page.click(self.submit_btn)

    def submit_form_with_data(self, name: str, email: str, subject: str, message: str, file_path: str = None) -> None:
        self.submit_form(name=name, email=email, subject=subject, message=message, file_path=file_path)

    def is_form_displayed(self) -> bool:
        return self.page.is_visible(self.submit_btn)

    def is_success_message_visible(self) -> bool:
        return self.page.is_visible(self.success_message)