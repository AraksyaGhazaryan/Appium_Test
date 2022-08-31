import sys
sys.path.append('/home/araksya/Appium_Project/Game/src/constants')
from const import selectors
import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


desired_cap = {
    "appPackage" : "com.example.android.guesstheword",
    "appActivity": ".MainActivity",
    "device" : "b1511ad",
    "os_version" : "9.0",
    "autoGrantPermissions":"true",
    "platformName": "Android",
    "autoAcceptAlerts":"true"
}


driver = webdriver.Remote(
command_executor="http://127.0.0.1:4723/wd/hub",
desired_capabilities=desired_cap
)

time.sleep(10)

play_button = driver.find_element(AppiumBy.ID, value=selectors['PLAY_BUTTON']).click()
assert driver.find_element(AppiumBy.ID, value=selectors['SKIP_BUTTON']).text=="SKIP"
skip = driver.find_element(AppiumBy.ID, value=selectors['SKIP_BUTTON']).click()
assert driver.find_element(AppiumBy.ID, value=selectors['GOT_IT']).text=="GOT IT"
got_it = driver.find_element(AppiumBy.ID, value=selectors['GOT_IT']).click()
assert driver.find_element(AppiumBy.ID, value=selectors['END_GAME']).text=="END GAME"
end_game = driver.find_element(AppiumBy.ID, value=selectors['END_GAME']).click()
assert driver.find_element(AppiumBy.ID, value=selectors['PLAY_AGAIN']).text=="PLAY AGAIN"
play_again = driver.find_element(AppiumBy.ID, value=selectors['PLAY_AGAIN']).click()
assert driver.find_element(AppiumBy.ID, value=selectors['SKIP_BUTTON']).text=="SKIP"
