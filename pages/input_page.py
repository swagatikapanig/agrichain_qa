from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from pages.result_page import ResultPage
from config import config


class InputPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.logo = page.locator("header img.logo")
        self.title = page.locator("header h1")
        self.login_link = page.get_by_role("link", name="Login")
        self.register_link = page.get_by_role("link", name="Register")
        self.string_input = page.locator("#string-input")
        self.submit_btn = page.locator("#submit-btn")

    def load(self) -> "InputPage":
        self.open(config.INPUT_PATH)
        expect(self.string_input).to_be_visible()
        return self

    def enter_string(self, value: str) -> "InputPage":
        self.string_input.fill(value)
        return self

    def submit(self) -> ResultPage:
        self.submit_btn.click()
        return ResultPage(self.page)

    def submit_string(self, value: str) -> ResultPage:
        return self.enter_string(value).submit()
