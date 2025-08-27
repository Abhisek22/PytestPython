import time
from types import LambdaType

from playwright.sync_api import Page


def test_handleAlerts(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    page.on("dialog", lambda dialog:dialog.accept())
    page.get_by_role("button",name="Alert").click()
    time.sleep(5)
