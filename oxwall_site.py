from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from page_objects import locators


class Oxwall:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)
        self.driver.maximize_window()
        self.driver.get('http://127.0.0.1/oxwall/')
        self.wait = WebDriverWait(self.driver, 10)
        self.actions = ActionChains(self.driver)

    def close(self):
        self.driver.quit()

    def login(self, username, password):
        self.driver.find_element(*locators.SIGN_IN_MENU).click()
        login = self.driver.find_element(*locators.LOGIN_FIELD)
        login.click()
        login.send_keys(username)
        passw = self.driver.find_element(*locators.PASS_FIELD)
        passw.click()
        passw.send_keys(password)
        self.driver.find_element(*locators.SIGN_IN_BUTTON).click()
        self.wait.until(EC.invisibility_of_element_located(locators.LOGIN_BACKGROUND))
        # wait.until_not(EC.visibility_of_element_located((By.ID, "floatbox_overlay")))

    def logout(self, user):
        menu = self.driver.find_element(By.LINK_TEXT, user.title())
        self.actions.move_to_element(menu).perform()
        self.driver.find_element(By.XPATH, './/a[contains(@href,"sign-out")]').click()
