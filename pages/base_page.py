from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page,):
        self.page = page

    def navigate(self, url: str):
        self.page.goto(url)
        self.dismiss_overlays()

    def dismiss_overlays(self) -> None:
        candidates = [
            "Consent",
            "I agree",
            "Agree",
            "Accept",
            "Accept all",
            "Allow all",
            "OK",
            "Got it",
        ]

        for name in candidates:
            try:
                btn = self.page.get_by_role("button", name=name)
                if btn.count() > 0 and btn.first.is_visible():
                    btn.first.click(timeout=500)
                    self.page.wait_for_timeout(200)
            except Exception:
                pass

    def go_back(self):
        self.page.go_back()

    def go_forward(self):
        self.page.go_forward()

    def reload(self):
        self.page.reload()

    def click(self, selector: str):
        self.page.click(selector)

    def fill(self, selector: str, text: str):
        self.page.fill(selector, text)

    def type(self, selector: str, text: str, delay: int=100):
        self.page.type(selector, text, delay=delay)

    def clear_and_type(self, selector: str, text: str):
        self.page.fill(selector, "")
        self.page.type(selector, text)

    def press_key(self, selector: str, key: str):
        self.page.press(selector, key)

    def check(self, selector: str):
        self.page.check(selector)

    def uncheck(self, selector: str):
        self.page.uncheck(selector)

    def select_option(self, selector: str, value: str):
        self.page.select_option(selector, value)

    def upload_file(self, selector: str, file_path: str):
        self.page.set_input_files(selector, file_path)

    # Assertions

    def is_visible(self, selector: str) -> bool:
        return self.page.is_visible(selector)

    def is_enabled(self, selector: str) -> bool:
        return self.page.is_enabled(selector)

    def get_text(self, selector: str) -> str:
        return self.page.locator(selector).inner_text().strip()

    def get_attribute(self, selector: str, attr: str) -> str:
        return self.page.get_attribute(selector, attr)

    def expect_text(self, selector: str, expected: str):
        expect(self.page.locator(selector)).to_have_text(expected)

    def set_viewport_size(self, width: int, height: int):
        self.page.set_viewport_size({"width": width, "height": height})

    def wait_for_selector(self, selector: str, timeout=5000):
        self.page.wait_for_selector(selector, timeout=timeout)

    def scroll_into_view(self, selector: str):
        self.page.locator(selector).scroll_into_view_if_needed()

    # JS evaluation
    def evaluate(self, script: str):
        return self.page.evaluate(script)

