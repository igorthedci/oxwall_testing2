from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("http://127.0.0.1/oxwall/")
        self.login(driver)
        driver.find_element_by_id("input_is1pupan").send_keys("New news!")
        driver.find_element_by_id("input_2wovevys").click()
        driver.find_element_by_xpath("//li[contains(@id,'action-feed')]/div/div[2]/div/div[3]").click()
        try:
            self.assertEqual("New news!", driver.find_element_by_xpath(
                "//li[contains(@id,'action-feed')]/div/div[2]/div/div[3]").text)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("//li[contains(@id,'action-feed')]/div/div[2]/div/div[2]").click()
        self.assertEqual("Admin", driver.find_element_by_xpath(
            "//li[contains(@id,'action-feed')]/div/div[2]/div/div[2]/a/b").text)
        driver.find_element_by_link_text("Sign Out").click()

    def login(self, driver):
        driver.find_element_by_xpath("//div[contains(@id, 'console_item_')]/span").click()
        driver.find_element_by_id("input_4ryg2b4s").click()
        driver.find_element_by_id("input_is1pupan").click()
        driver.find_element_by_id("input_is1pupan").clear()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
