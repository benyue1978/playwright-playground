"""
Test suite for joinhorizons.com main navigation bar UI.
"""

import pytest
from playwright.sync_api import Page, expect
from tests.utils import find_first_visible

NAV_ITEMS = [
    "Platform",
    "Pricing",
    "Coverage",
    "Partnership",
    "About",
    "Resources",
]

@pytest.mark.e2e
def test_main_navbar_items_visible_and_clickable(page: Page) -> None:
    """
    Verify that each main navigation bar item is visible and clickable.
    """
    page.goto("https://joinhorizons.com/", wait_until="domcontentloaded", timeout=60000)
    header = page.locator('[data-elementor-type="header"]')
    for item in NAV_ITEMS:
        nav_links = header.get_by_text(item, exact=True)
        nav_link = find_first_visible(nav_links)
        expect(nav_link).to_be_enabled()
