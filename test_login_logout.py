from oxwall_site_model import OxwallSite
from page_objects.dashboard_page import DashboardPage
from page_objects.main_page import MainPage
from page_objects.signing_in_page import SignInPage
from value_models.user import User


# TODO: parametrize to users, add non-admin users
def test_positive_login(driver):
    user = User(username="admin", password="pass")
    app = OxwallSite(driver)
    app.login_as(user)
    # TODO: verification that logged in, example: app.is_logged_in_as(user) or app.user_menu_is_present()
    assert True
    # TODO: verification that correct page is opened, example from Nazar: app.active_page == "DASHBOARD"
    assert True
    app.logout_as(user)
    # TODO: verification, again, other menu and page
    assert True


# TODO: parametrize to users, add non-admin users
def test_login_using_page_object(driver):
    user = User(username="admin", password="pass")
    main_page = MainPage(driver)
    main_page.sign_in_menu.click()
    sign_in_page = SignInPage(driver)
    assert sign_in_page.is_this_page()
    sign_in_page.input_username(user.username)
    sign_in_page.input_password(user.password)
    sign_in_page.submit_form()
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.is_this_page()
    assert dashboard_page.is_logged_in()
    assert dashboard_page.is_logged_in_as(user)
