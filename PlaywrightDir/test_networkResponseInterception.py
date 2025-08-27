from playwright.sync_api import Page

fakePayloadOrderResponse = {"data": [], "message": "No Orders"}

def InterceptResponse(route):
    route.fulfill(
        json = fakePayloadOrderResponse
    )

def test_ResponseInterception(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", InterceptResponse)
    page.locator("#userEmail").fill("abhisekghosh22@gmail.com")
    page.locator("#userPassword").fill("Password123")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    order_text = page.locator(".mt-4").text_content()
    print(order_text)


