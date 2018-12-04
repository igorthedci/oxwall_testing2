def test_add_text_status(app, sign_in_session):
    test_text = "Shit happens!!!:("
    expected_text = test_text[-2]

    app.add_new_text_status(test_text)
    app.wait_until_new_status_appeared()
    # Verification that new status with this text appeared
    text_elements = app.get_newsfeed_list()
    assert text_elements[0].text == expected_text
