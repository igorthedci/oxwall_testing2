# TODO clean all these old imports after using new PageObjects approach
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from locators.locator import InternalPageLocators, SignInLocators
import time

from page_objects.dashboard_page import DashboardPage
from page_objects.main_page import MainPage
from page_objects.signing_in_page import SignInPage


class OxwallSite:
    def __init__(self, driver):
        # Open Oxwall site
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.dash_page = DashboardPage(self.driver)
        self.sign_in_page = SignInPage(self.driver)


    # Now these actions are in Page Objects.
    # TODO: clean all this old code, and use new approach in all parts of project
        self.wait = WebDriverWait(self.driver, 10)
        self.actions = ActionChains(self.driver)

    def login_as(self, user):
        # TODO: use Page objects
        """ Login to Oxwall site by user"""
        driver = self.driver
        driver.find_element(*InternalPageLocators.SIGN_IN_MENU).click()
        login = driver.find_element(*SignInLocators.LOGIN_FIELD)
        login.click()
        login.send_keys(user.username)
        passw = driver.find_element(*SignInLocators.PASS_FIELD)
        passw.click()
        passw.send_keys(user.password)
        driver.find_element(*SignInLocators.SIGN_IN_BUTTON).click()
        # Wait until grey background disappeared
        wait = WebDriverWait(driver, 5)
        wait.until(EC.invisibility_of_element_located(SignInLocators.LOGIN_BACKGROUND))

    def logout_as(self, user):
        # TODO: use Page objects
        menu = self.driver.find_element(*InternalPageLocators.USER_MENU)
        self.actions.move_to_element(menu).perform()
        self.driver.find_element(*InternalPageLocators.SIGN_OUT_LINK).click()

    @allure.step("WHEN I add a status with {status} in Dashboard page")
    def add_new_text_status(self, status):
        self.dash_page.status_text_field.input(status.text)
        self.dash_page.send_button.click()

    @allure.step('Then this status block has this {status.text} and author {user.real_name} '
                 'and time "within 1 minute"')
    def verify_text_status(self, status):
        new_status = self.dash_page.status_list[0]
        assert status.text == new_status.text
        assert status.user.real_name == new_status.user
        assert "within 1 minute" == new_status.time