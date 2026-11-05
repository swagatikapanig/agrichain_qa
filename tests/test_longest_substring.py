import re
import pytest
from playwright.sync_api import expect
from longest_substring import length_of_longest_substring


@pytest.mark.smoke
@pytest.mark.parametrize("text, expected", [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    ("abba", 2),
    ("dvdf", 3),
])
def test_longest_substring_end_to_end(input_page, text, expected):
    """User enters a string on /qa/input, clicks Submit, and sees the
    correct length on /qa/result."""
    assert length_of_longest_substring(text) == expected  # validate test data

    result_page = input_page.submit_string(text)

    result_page.expect_loaded()
    result_page.expect_output(expected)


@pytest.mark.regression
def test_back_to_home_returns_to_input_page(input_page):
    result_page = input_page.submit_string("abcabcbb")
    result_page.expect_loaded()

    home = result_page.go_back_home()

    expect(home.page).to_have_url(re.compile("/qa/input"))
    expect(home.string_input).to_have_value("")
