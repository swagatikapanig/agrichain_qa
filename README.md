# Agrichain QA

A Python-based automation framework using 
- Playwright and Pytest to simulate user input workflows across custom routes (`/qa/input` and `/qa/result`). 
- Structured the project using Page Object Model design patterns to maintain separation between test logic and locators, while enabling configurable test execution across multiple browsers and test suites (including smoke tests).

Problem 1 solution (`longest_substring.py`) and a Playwright + pytest framework for the Agrichain string-input site. Locators are assumed from the wireframe since there is no live site.

## Structure
```
├── longest_substring.py          # Problem 1
├── config/config.py              # base URL, paths
├── pages/
│   ├── base_page.py              # shared navigation
│   ├── input_page.py             # /qa/input elements + actions
│   └── result_page.py            # /qa/result elements + assertions
├── tests/
│   ├── conftest.py               # fixtures
│   └── test_longest_substring.py # scenarios
├── pytest.ini
└── requirements.txt
```

## Run
```bash
pip install -r requirements.txt
playwright install
pytest                                # all tests
pytest -m smoke                       # smoke only
pytest --browser firefox --headed     # other browser, visible
```
