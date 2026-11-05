from playwright.sync_api import Page
from config import config


class BasePage:
    """Shared behaviour. Playwright auto-waits on actions, so no wait helpers needed."""

    def __init__(self, page: Page):
        self.page = page

    def open(self, path: str = ""):
        self.page.goto(config.BASE_URL + path)
