"""
Test suite for joinhorizons.com homepage UI.
"""

import pytest
from playwright.sync_api import Page
from tests.utils import find_first_visible

@pytest.mark.e2e
def test_homepage_logo_visible(page: Page) -> None:
    """
    Verify the home page loads successfully and the logo is visible.
    """
    page.goto("https://joinhorizons.com/", wait_until="domcontentloaded", timeout=60000)
    logos = page.locator("a[href='https://joinhorizons.com/'] img[alt='horizons logo']")
    logo = find_first_visible(logos)
    assert logo.get_attribute("src") == "https://joinhorizons.com/wp-content/uploads/2022/09/logo-black.svg"
