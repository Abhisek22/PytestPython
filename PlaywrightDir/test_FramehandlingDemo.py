import time

from playwright.sync_api import Page, expect


def test_FrameHandling(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    pageFrame = page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link", name="All Access plan").click()
    expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers")
    time.sleep(5)
