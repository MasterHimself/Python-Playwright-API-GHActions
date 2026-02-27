from playwright.sync_api import Page

from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.logo_selector = "//img[@alt='Website for automation practice']"
        self.products_button = "//a[@href='/products']"

    def is_logo_visible(self) -> bool:
        return self.page.is_visible(self.logo_selector)

    def click_products(self) -> None:
        self.page.click(self.products_button)