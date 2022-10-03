from src.PageObject.errors.errors_for_game_page import errors_for_game_page
from src.PageObject.pages.game_page_factory import *
from src.TestBase.utils.driver_setup import driver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
import pytest


base_page =BasePage(driver)

@pytest.title('Verify "Skip button" is it add word in page')
@pytest.description("""
Verify "Skip button" is it add word page after clicking
""")
def test_verify_skip_button():
    game_page = base_page.click_on_play()
    assert game_page, errors_for_game_page['skip_button_is_not_displayed']

  

@pytest.title('Verify "Go it button" is it add word in page')
@pytest.description("""
Verify "Skip button" is it add word result page after clicking
""")
def test_verify_skip_button():
    game_page = base_page.click_on_skip()
    assert game_page, errors_for_game_page['got_it_button_is_not_displayed']
      


@pytest.title('Verify "End game button" is it add word in page')
@pytest.description("""
Verify "End game button" is it add word result page after clicking
""")
def test_verify_end_game_button():
    game_page = base_page.click_on_end_game()
    assert game_page, errors_for_game_page['end_game_button_is_not_displayed']
            