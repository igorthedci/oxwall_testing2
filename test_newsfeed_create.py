from oxwall_site_model import OxwallSite
from value_models.status import Status


# TODO parametrize Status text
def test_add_text_status(driver, signed_in_user):
    status = Status(text="Shit happens!!!:(", user=signed_in_user)
    app = OxwallSite(driver)
    app.add_new_text_status(status.text)
    app.wait_until_new_status_appeared()
    # Verification that new status with this text appeared
    text_elements = app.get_newsfeed_list()
    newsfeed_users = app.get_newsfeed_users()
    newsfeed_times = app.get_newsfeed_times()
    assert text_elements[0].text == status.text
    assert newsfeed_users[0].text == status.user.real_name
    assert newsfeed_times[0].text == "within 1 minute"
