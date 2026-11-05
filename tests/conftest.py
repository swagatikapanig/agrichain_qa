import sys, pathlib
import pytest

# make project root importable (config, pages, longest_substring)
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))

from pages.input_page import InputPage


@pytest.fixture
def input_page(page):
    """`page` is provided by pytest-playwright (browser + context + page,
    created and closed automatically). Browser choice: --browser chromium|firefox|webkit."""
    return InputPage(page).load()
