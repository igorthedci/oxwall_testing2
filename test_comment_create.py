import time


def test_add_comment(app, login_user):
    test_text = "Shit happens!!!:("
    expected_text = test_text
    newsfeed = app.driver.find_element_by_name("status")
    newsfeed.click()
    newsfeed.clear()
    newsfeed.click()
    newsfeed.send_keys(test_text)
    send_button = app.driver.find_element_by_name("save")
    send_button.click()
    time.sleep(2)
    # Verifications
    text_element = app.driver.find_elements_by_class_name("ow_newsfeed_content")
    print(text_element[0].text)
    assert text_element[0].text == expected_text

