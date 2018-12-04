import time


def test_add_text_status(driver, login, logout):
    test_text = "Shit happens!!!:("
    expected_text = test_text[-2]

    # Write some text to Newsfeed form and send it
    newsfeed = driver.find_element_by_name("status")
    newsfeed.click()
    newsfeed.clear()
    newsfeed.click()
    newsfeed.send_keys(test_text)
    send_button = driver.find_element_by_name("save")
    send_button.click()

    # Wait until new status appear
    time.sleep(2)

    # Verification that new status with this text appeared
    text_element = driver.find_elements_by_class_name("ow_newsfeed_content")
    assert text_element[0].text == expected_text
