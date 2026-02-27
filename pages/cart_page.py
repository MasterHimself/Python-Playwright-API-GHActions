from playwright.sync_api import Page

from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.cart_items = "//div[@id='cart_info']"
        self.checkout_button = ".check_out"
        self.empty_cart_text = "Cart is empty!"

    def is_cart_items_visible(self) -> bool:
        return self.page.is_visible(self.cart_items)

    def proceed_to_checkout(self) -> None:
        self.page.click(self.checkout_button)

    def get_title(self) -> str:
        return self.page.title()

    def is_cart_text_present(self) -> bool:
        if self.page.get_by_text(self.empty_cart_text, exact=False).count() > 0:
            return self.page.get_by_text(self.empty_cart_text, exact=False).first.is_visible()
        return self.page.is_visible(self.cart_items)