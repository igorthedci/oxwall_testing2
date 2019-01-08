import time
from selenium.webdriver.common.by import By

from page_objects.internal_page import InternalPage


class DashboardPage(InternalPage):
    STATUS_TEXT_FIELD = (By.NAME, "status")
    SEND_BUTTON = (By.NAME, "save")
    STATUS_BOX = (By.XPATH, "//li[contains(@id, 'action-feed')]")

    # TODO Add all elements and actions that you have in Dashboard Page

    def is_this_page(self):
        return self.active_menu.text == "DASHBOARD"

    @property
    def status_text_field(self):
        return self.find_visible_element(self.STATUS_TEXT_FIELD)

    @property
    def send_button(self):
        return self.find_visible_element(self.SEND_BUTTON)

    @property
    def status_list(self):
        return self.driver.find_elements(*self.STATUS_BOX)

    def wait_until_new_status_appeared(self):
        # TODO You need to do smart explicit wait!!!
        time.sleep(5)
