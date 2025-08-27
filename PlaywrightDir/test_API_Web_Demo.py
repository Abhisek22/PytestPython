from playwright.sync_api import Playwright, expect

from PlaywrightDir.Utils.apiBase import APIUtils


def test_e2e_api_web(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #create order -> Fetch Order Id using API calls

    api_utils = APIUtils()
    orderId = api_utils.create_order(playwright)

    #Application login through UI
    page.goto("https://rahulshettyacademy.com/client")
    page.locator("#userEmail").fill("abhisekghosh22@gmail.com")
    page.locator("#userPassword").fill("Password123")
    page.get_by_role("button",name="Login").click()
    page.get_by_role("button", name="Orders").click()

    #validate the order id created is available in Order History
    page.locator("tr").filter(has_text=orderId).get_by_role("button",name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    context.close()