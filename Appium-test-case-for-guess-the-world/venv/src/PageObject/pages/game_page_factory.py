from src.PageObject.constants.game_consts import selectors_game_page
from src.TestBase.utils.driver_setup import driver
from appium.webdriver.common.appiumby import AppiumBy

class GamePage():
    def __init__(self, driver):
        self.driver = driver
        self.skip = driver.find_element(AppiumBy.ID, value=selectors['SKIP_BUTTON']) 
        self.got_it = driver.find_element(AppiumBy.ID, value=selectors['GOT_IT'])
        self.end_game = driver.find_element(AppiumBy.ID, value=selectors['END_GAME'])



    def click_on_skip(self):
        self.skip.click()


    def click_on_got_it(self):
        self.got_it.click()    
    

    def click_on_end_game(self):
        self.end_game.click()     

