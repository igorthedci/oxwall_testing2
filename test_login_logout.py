from oxwall_site_model import OxwallSite
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