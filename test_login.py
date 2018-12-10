from oxwall_site_model import OxwallSite
from page_object.internal_pages import InternalPage
from page_object.signin_page import SignInPage


def test_positive_login(driver, user):
    internal_page = InternalPage(driver)
    internal_page.sign_in_menu.click()

    signin_page = SignInPage(driver)
    signin_page.input_username_to_login_form(user.username)
    signin_page.input_password_to_login_form(user.password)
    signin_page.submit_form()
    assert internal_page.is_logged_in()
    assert internal_page.active_menu.text == "DASHBOARD"

