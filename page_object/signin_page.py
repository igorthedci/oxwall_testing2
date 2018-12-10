from page_object.page import Page
from page_object.locator import SignInLocators


class SignInPage(Page):
    # def __init__(self, driver):
    #     super().__init__(driver)
    #     self.username_field = self.find_visible_element(locator.LOGIN_FIELD)

    @property
    def username_field(self):
        return self.find_visible_element(SignInLocators.LOGIN_FIELD)

    @property
    def password_field(self):
        return self.find_visible_element(SignInLocators.PASS_FIELD)

    @property
    def sign_in_button(self):
        return self.find_visible_element(SignInLocators.SIGN_IN_BUTTON)

    def input_username_to_login_form(self, username):
        self.username_field.send_keys(username)

    def input_password_to_login_form(self, password):
        self.password_field.send_keys(password)

    def submit_form(self):
        self.sign_in_button.click()






if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Chrome()
    singn_in_page = SignInPage(driver)
    singn_in_page.username_field.send_keys("hjbjhb")
    singn_in_page.username_field.click()