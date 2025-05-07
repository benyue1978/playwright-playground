"""
Test suite for 'Book a demo' buttons on joinhorizons.com.
"""

import pytest
from playwright.sync_api import Page, expect
from tests.utils import find_first_visible
from typing import List, Tuple
import os

SCREENSHOT_DIR = "tests/screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

@pytest.mark.e2e
def test_all_book_a_demo_buttons_open_dialog(page: Page) -> None:
    """
    Verify all 'Book a demo' buttons/links open a dialog. If not, fail and include URL.
    On failure, take a snapshot and highlight the button.
    """
    page.goto("https://joinhorizons.com/", wait_until="domcontentloaded", timeout=60000)
    page.wait_for_function("document.readyState === 'complete'", timeout=60000)

    buttons = page.locator("a:has-text('Book a demo'), button:has-text('Book a demo')")
    count = buttons.count()
    visible_indices = []
    for i in range(count):
        btn = buttons.nth(i)
        if btn.is_visible():
            visible_indices.append(i)
    assert visible_indices, "No visible 'Book a demo' button or link found on the page."

    failed_buttons: List[Tuple[int, str, str, str]] = []
    for i in visible_indices:
        button = buttons.nth(i)
        # 等待按钮可见且可用
        expect(button).to_be_visible(timeout=5000)
        expect(button).to_be_enabled(timeout=5000)
        #button.hover()
        href = button.get_attribute("href")
        if not href:
            parent_a = button.locator("xpath=ancestor::a[1]")
            href = parent_a.get_attribute("href") if parent_a.count() > 0 else None
        original_url = page.url

        button.click()
        failed = False

        if page.url != original_url:
            failed = True
            page.goto(original_url, wait_until="domcontentloaded", timeout=60000)
            page.wait_for_function("document.readyState === 'complete'", timeout=60000)
        else:
            try:
                # 等待弹窗 DOM 存在
                page.wait_for_selector('.elementor-popup-modal[aria-modal="true"]', timeout=5000)
                dialog = page.locator('.elementor-popup-modal[aria-modal="true"]')
                expect(dialog).to_be_visible(timeout=2000)
            except Exception:
                failed = True

        if failed:
            screenshot_path = os.path.join(SCREENSHOT_DIR, f"book_a_demo_{i}.png")
            highlight_and_screenshot(page, button, screenshot_path)
            failed_buttons.append((i, href or "(no href)", page.url, screenshot_path))
            continue

        close_btn = page.locator('.dialog-close-button[aria-label="Close"]')
        if close_btn.count() > 0:
            find_first_visible(close_btn).click()
            page.wait_for_timeout(500)
    if failed_buttons:
        fail_info = ", ".join([
            f"index {idx} (href: {url}, landed: {landed}, screenshot: {shot})"
            for idx, url, landed, shot in failed_buttons
        ])
        pytest.fail(f"'Book a demo' button(s) failed to open a dialog: {fail_info}. Start Page URL: {page.url}")

def highlight_and_screenshot(page: Page, locator, path: str) -> None:
    """
    Highlight the first visible element and take a full page screenshot.
    Restore the element's original style after the screenshot.
    Wait until highlight style is applied before taking the screenshot.
    Ensure the element is scrolled into view and visible on screen.
    """
    handle = None
    try:
        handle = locator.element_handle()
        if handle:
            # 滚动到元素
            handle.evaluate(
                '''
                el => el.scrollIntoView({behavior: 'auto', block: 'center'})
                '''
            )
            # 检查中心点在视口内且未被遮挡
            page.wait_for_function(
                '''
                el => {
                    const rect = el.getBoundingClientRect();
                    const cx = rect.left + rect.width / 2;
                    const cy = rect.top + rect.height / 2;
                    if (cx < 0 || cy < 0 || cx > window.innerWidth || cy > window.innerHeight) return false;
                    const topElem = document.elementFromPoint(cx, cy);
                    return el === topElem || el.contains(topElem);
                }
                ''',
                arg=handle,
                timeout=2000
            )
            # 设置高亮样式
            handle.evaluate(
                '''
                el => {
                    el.setAttribute("data-playwright-highlight", "1");
                    el.style.setProperty('box-shadow', '0 0 0 6px #ff0, 0 0 16px 12px #f00, 0 0 32px 24px #ff0', 'important');
                    el.style.setProperty('outline', '6px solid #ff0000', 'important');
                    el.style.setProperty('background', 'rgba(255,255,0,0.5)', 'important');
                    el.style.setProperty('z-index', '2147483647', 'important');
                    el.style.setProperty('position', 'relative', 'important');
                }
                '''
            )
            # 用 JS 检查高亮样式是否生效
            page.wait_for_function(
                """el => {
                    const style = window.getComputedStyle(el);
                    return style.outline.includes('rgb(255, 0, 0)') &&
                           style.backgroundColor.includes('rgba(255, 255, 0, 0.5)');
                }""",
                arg=handle,
                timeout=2000
            )
            # 截图
            page.screenshot(path=path)
            print("screenshot done")
        else:
            page.screenshot(path=path, full_page=True)
    except Exception as e:
        print("Highlight failed:", e)
        page.screenshot(path=path, full_page=True)
    finally:
        if handle:
            handle.dispose() 