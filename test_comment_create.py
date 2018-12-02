def test_add_comment(app, login_user):
    test_text = "Shit happens!!!:("
    expected_text = test_text[-2]
    app.create_comment(test_text)
    # Verifications
    comments_elements = app.get_comments()
    assert comments_elements[0].text == expected_text


# Тот же тест написанній низкоуровневым кодом (для сравнения)
import time

def test_add_comment2(driver, login_low_level):
    test_text = "Shit happens!!!:("
    expected_text = test_text[-2]
    newsfeed = driver.find_element_by_name("status")
    newsfeed.click()
    newsfeed.clear()
    newsfeed.click()
    newsfeed.send_keys(test_text)
    send_button = driver.find_element_by_name("save")
    send_button.click()
    time.sleep(2)
    # Verifications
    text_element = driver.find_elements_by_class_name("ow_newsfeed_content")
    print(text_element[0].text)
    assert text_element[0].text == expected_text