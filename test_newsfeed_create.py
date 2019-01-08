from oxwall_site_model import OxwallSite
from value_models.status import Status


# TODO parametrize Status text
def test_add_text_status(driver, signed_in_user):
    status = Status(text="Shit happens!!!:(", user=signed_in_user)
    app = OxwallSite(driver)
    old_status_list = app.dash_page.status_list

    app.dash_page.status_text_field.send_keys(status.text)
    app.dash_page.send_button.click()
    app.dash_page.wait_until_new_status_appeared()

    new_status_list = app.dash_page.status_list
    assert len(new_status_list) == len(old_status_list) + 1
    assert status.text in new_status_list[0].text
    assert signed_in_user.real_name in new_status_list[0].text
    assert "within 1 minute" in new_status_list[0].text
    # Verification that new status with this text appeared
    # text_elements = app.get_newsfeed_list()
    # newsfeed_users = app.get_newsfeed_users()
    # newsfeed_times = app.get_newsfeed_times()
    # assert text_elements[0].text == status.text
    # assert newsfeed_users[0].text == status.user.real_name
    # assert newsfeed_times[0].text == "within 1 minute"
