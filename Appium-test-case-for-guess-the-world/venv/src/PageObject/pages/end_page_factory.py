from src.PageObject.constants.start_consts import selectors_start_page
from src.TestBase.utils.driver_setup import driver
#from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


class EndPage():
    def __init__ (self, driver):
        self.driver = driver
        self.play_again = driver.find_element(AppiumBy.ID, value=selectors['PLAY_AGAIN'])


    def click_on_play_again(self):
        self.play_again.click()    
