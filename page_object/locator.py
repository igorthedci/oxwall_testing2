from selenium.webdriver.common.by import By

class InternalPageLocators:
    ACTIVE_MENU = (By.XPATH, "//div[contains(@class, 'ow_menu_wrap')]//li[contains(@class, 'active')]")
    MAIN_MENU = ()
    DASHBOARD_MENU = (By.LINK_TEXT, "DASHBOARD")
    SIGN_IN_MENU = (By.XPATH, '//*[contains(@id,"console_item")]/span[1]')
    SIGN_OUT_MENU = (By.XPATH, './/a[contains(@href,"sign-out")]')
    USER_MENU = (By.XPATH, "//div[contains(@class,'ow_console_dropdown_hover')]")

class SignInLocators:
    LOGIN_FIELD = (By.NAME, 'identity')
    PASS_FIELD = (By.NAME, 'password')
    SIGN_IN_BUTTON = (By.XPATH, "//div[@class='ow_right']")
    LOGIN_BACKGROUND = (By.ID, "floatbox_overlay")



# Newsfeed page_object ...

# Registration page_object ...
