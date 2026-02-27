from playwright.sync_api import Page

from pages.base_page import BasePage


class SignupLoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.signup_name_input = "//input[@placeholder='Name']"
        self.signup_email_input = "//input[@data-qa='signup-email']"
        self.signup_button = "//button[@data-qa='signup-button']"
        self.login_email_input = "//input[@data-qa='login-email']"
        self.login_password_input = "//input[@data-qa='login-password']"
        self.login_button = "//button[@data-qa='login-button']"

    def signup(self, name: str, email: str) -> None:
        self.page.fill(self.signup_name_input, name)
        self.page.fill(self.signup_email_input, email)
        self.page.click(self.signup_button)

    def login(self, email: str, password: str) -> None:
        self.page.fill(self.login_email_input, email)
        self.page.fill(self.login_password_input, password)
        self.page.click(self.login_button)

    def is_login_form_visible(self) -> bool:
        return self.page.is_visible(self.login_button)

    def is_login_error_visible(self) -> bool:
        return self.page.get_by_text("Your email or password is incorrect", exact=False).first.is_visible()