from oxwall_site_model import OxwallSite


# TODO: parametrize to users, add non-admin users
def test_login_using_page_object(driver, user):
    app = OxwallSite(driver)
    app.main_page.sign_in_click()
    assert app.sign_in_page.is_this_page()
    app.sign_in_page.input_username(user.username)
    app.sign_in_page.input_password(user.password)
    app.sign_in_page.submit_form()
    assert app.dash_page.is_this_page()
    assert app.dash_page.is_logged_in()
    assert app.dash_page.user_menu.text == user.real_name
