import pytest

from oxwall_site_model import OxwallSite
from value_models.status import Status
from data.status_data import status_data


@pytest.mark.parametrize("status_text", status_data)
def test_add_text_status(driver, signed_in_user, status_text, db):
    status = Status(text=status_text, user=signed_in_user)
    app = OxwallSite(driver)
    old_status_amount = db.count_news()
    # Actions:
    app.dash_page.status_text_field.input(status.text)
    app.dash_page.send_button.click()
    app.dash_page.wait_until_new_status_appeared()
    # Verification that new status with this text appeared
    assert db.count_news() == old_status_amount + 1
    assert status.text == db.get_last_news().text
    new_status = app.dash_page.status_list[0]
    assert status.text == new_status.text
    assert signed_in_user.real_name == new_status.user
    assert "within 1 minute" == new_status.time
