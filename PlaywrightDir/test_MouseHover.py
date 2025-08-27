from playwright.sync_api import Page


def test_MouseHover(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.locator("#mousehover").hover()
    page.get_by_role("link", name="Top").click()