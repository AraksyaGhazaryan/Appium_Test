from appium import webdriver


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