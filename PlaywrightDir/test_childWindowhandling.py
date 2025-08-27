
from playwright.sync_api import Page


def test_childWindowHandle(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    with page.expect_popup() as new_PageInfo:
        page.locator(".blinkingText").click()
        childPage = new_PageInfo.value
        text = childPage.locator(".red").text_content()
        print(text)
        word = text.split("at")
        email = word[1].strip().split(" ")[0]
        assert email == "mentor@rahulshettyacademy.com"

