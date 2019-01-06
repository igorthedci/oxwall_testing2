from page_objects.dashboard_page import DashboardPage
from page_objects.main_page import MainPage
from page_objects.signing_in_page import SignInPage


# TODO: parametrize to users, add non-admin users
def test_login_using_page_object(driver, user):
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
