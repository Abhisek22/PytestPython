import time

from playwright.sync_api import Page

def InterceptRequest(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=68af3dfff669d6cb0aa04a72")

def test_RequestInterception(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", InterceptRequest)
    page.locator("#userEmail").fill("abhisekghosh22@gmail.com")
    page.locator("#userPassword").fill("Password123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    time.sleep(5)
    message = page.locator(".blink_me").text_content()
    print(message)


