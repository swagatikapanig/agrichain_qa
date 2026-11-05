import re
from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from config import config


class ResultPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.output_label = page.locator("#output-label")      # "Output is:"
        self.output_value = page.locator("#output-value")      # Let say "3"
        self.back_to_home_btn = page.locator("#back-home-btn")

    def expect_loaded(self):
        expect(self.page).to_have_url(re.compile(config.RESULT_PATH))
        expect(self.output_value).to_be_visible()

    def expect_output(self, expected: int):
        # web-first assertion: retries until text matches or timeout
        expect(self.output_value).to_have_text(str(expected))

    def go_back_home(self):
        from pages.input_page import InputPage
        self.back_to_home_btn.click()
        return InputPage(self.page)
