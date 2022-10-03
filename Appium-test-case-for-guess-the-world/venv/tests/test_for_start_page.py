from src.PageObject.errors.errors_for_start_page import errors_for_start_page
from src.PageObject.pages.start_page import *
from src.TestBase.utils.driver_setup import driver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
import pytest



base_page =BasePage(driver)

@pytest.title('Verify "Play button" is it open Game result page')
@pytest.description("""
Verify "Play button" is it open Game result page after clicking
""")
def test_verify_play_button():
    start_page = base_page.click_on_play()
    assert start_page, errors_for_start_page['start_page_is_not_existing']
   