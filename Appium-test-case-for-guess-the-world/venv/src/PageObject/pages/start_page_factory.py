from src.PageObject.constants.start_consts import selectors_start_page
from src.TestBase.utils.driver_setup import driver
from appium.webdriver.common.appiumby import AppiumBy


class StartPage():
    def __init__(self, driver):
        self.driver = driver
        self.play = driver.find_element(AppiumBy.ID, value=selectors['PLAY_BUTTON'])

    def click_on_play(self):
        self.play.click()
