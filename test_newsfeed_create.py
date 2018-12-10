from oxwall_site_model import OxwallSite
from value_models.status import Status


def test_add_text_status(driver, sign_in_session, admin_user):
    app = OxwallSite(driver)
    status = Status(text="text", user=admin_user)

    app.add_new_text_status(status)
    app.wait_until_new_status_appeared()
    # Verification that new status with this text appeared

    text_elements = app.get_newsfeed_list()
    user_status_elements = app.get_status_users()
    time_status_elements = app.get_status_users()
    assert status_block.status_text == status.text
    assert status_block.user_element.text == status.user.real_name
    assert status_block.time_element.text == "within 1 minute"
