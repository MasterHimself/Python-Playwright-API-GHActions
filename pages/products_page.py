from playwright.sync_api import Page

from pages.base_page import BasePage


class ProductsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.search_input = "//input[@id='search_product']"
        self.search_button = "//button[@id='submit_search']"
        self.product_list = "//div[@class='features_items']"

    def search_product(self, product_name: str) -> None:
        self.page.fill(self.search_input, product_name)
        self.page.click(self.search_button)

    def search(self, product_name: str) -> None:
        self.search_product(product_name)

    def is_product_list_visible(self) -> bool:
        try:
            self.page.wait_for_selector(self.product_list, timeout=10000)
        except Exception:
            pass
        return self.page.is_visible(self.product_list)

    def is_search_result_displayed(self) -> bool:
        return self.is_product_list_visible()