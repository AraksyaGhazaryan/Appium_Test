from src.PageObject.errors.errors_for_end_page import  errors_for_end_page
from src.PageObject.pages.create_page_factory import *
from src.PageObject.pages.base_page import *
from src.TestBase.utils.driver_setup import driver
from appium.webdriver.common.appiumby import AppiumBy
#from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
import pytest

base_page =BasePage(driver)

@pytest.title('Verify "Play again" is it open Game result page')
@pytest.description("""
Verify "Play again" is it open Game result page after clicking
""")
def test_verify_play_again_button():
    end_page = base_page.click_on_play_again()
    assert end_page, errors_for_end_page['play_again_button_is_not_displayed']
    


