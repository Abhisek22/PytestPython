import time

from playwright.sync_api import Page, expect, Playwright


def test_PlaywrightBasicFunction(playwright):  #"playwright" is a global fixture from "playwright.paytest" package which we are invoking while defining test function
    browser = playwright.chromium.launch(headless=False)  #Invoking browser engine in Incognito mode. Chromium supports both Chrome and Edge browser engines
    context = browser.new_context()  #Invoking tht browser engine to open a new tab with new context
    page = context.new_page()  #Invoking the context to open a new page in the browser tab
    page.goto("https://rahulshettyacademy.com")  #Hitting the url in the new browser page to open the application link

def test_PlaywrightShortcutFunction(page:Page):
    page.goto("https://rahulshettyacademy.com")

def test_CoreLocators(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("consult")
    page.locator("#terms").check()
    page.get_by_role("button",name="Sign In").click()
    time.sleep(10)
 #   expect(page.get_by_text("ProtoCommerce Home")).to_be_visible()
    expect(page.get_by_role("link", name="ProtoCommerce Home")).to_be_visible()

def test_FirefoxBrowserFunction(playwright : Playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("consult")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    time.sleep(10)