from playwright.sync_api import Page, expect


def test_Webtables(page:Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    #finding the web column having the header value as "Price"
    for items in range(page.locator("th").count()):
        if page.locator("th").nth(items).filter(has_text="Price").count()>0:
            priceColNum = items
            print(f"Price Column Number is {priceColNum}")
            break

    riceRow = page.locator("tr").filter(has_text="Rice")
#    print(f"Rice Row Number is {riceRow}")
    expect(riceRow.locator("td").nth(priceColNum)).to_have_text("37")