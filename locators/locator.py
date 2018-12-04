from selenium.webdriver.common.by import By

# Main menu locators
SIGN_IN_MENU = (By.XPATH, '//*[contains(@id,"console_item")]/span[1]')
SIGN_OUT_MENU = ()

# Login windows locators
LOGIN_FIELD = (By.NAME, 'identity')
PASS_FIELD = (By.NAME, 'password')
SIGN_IN_BUTTON = (By.XPATH, "//div[@class='ow_right']")
LOGIN_BACKGROUND = (By.ID, "floatbox_overlay")

# Newsfeed locators ...

# Registration locators ...
