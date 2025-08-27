from playwright.sync_api import Playwright, expect

from PlaywrightDir.Utils.apiBase import APIUtils


def test_session_storage(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    api_utils = APIUtils()
    getToken = api_utils.get_token(playwright)
    page.add_init_script(f"""localStorage.setItem('token','{getToken}')""")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()