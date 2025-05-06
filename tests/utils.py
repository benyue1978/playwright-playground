"""
Utility functions for Playwright UI tests.
"""

from playwright.sync_api import Locator
from typing import Optional

def find_first_visible(locator: Locator) -> Optional[Locator]:
    """
    Return the first visible element from a Locator collection.
    Raise AssertionError if none are visible.
    """
    count = locator.count()
    for i in range(count):
        el = locator.nth(i)
        if el.is_visible():
            return el
    raise AssertionError("No visible element found in locator collection.") 