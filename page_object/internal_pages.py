from selenium.common.exceptions import NoSuchElementException
from page_object.locator import InternalPageLocators
from page_object.page import Page


class InternalPage(Page):
    def is_logged_in(self):
        return self.is_element_present(InternalPageLocators.DASHBOARD_MENU)

    @property
    def active_menu(self):
        return self.find_visible_element(InternalPageLocators.ACTIVE_MENU)


    @property
    def sign_in_menu(self):
        if not self.is_logged_in():
            return self.find_visible_element(InternalPageLocators.SIGN_IN_MENU)
        else:
            raise NoSuchElementException("No element by locator {}".format(InternalPageLocators.SIGN_IN_MENU))

    @property
    def sign_out_button(self):
        if self.is_logged_in():
            return self.find_visible_element(InternalPageLocators.SIGN_OUT_MENU)

    @property
    def user_menu(self):
        return self.find_visible_element(InternalPageLocators.USER_MENU)

    def sign_out(self):
        self.action.move_to_element(self.user_menu).perform()
        self.sign_out_button.click()

