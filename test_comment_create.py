def test_add_comment(app, login_user):
    test_text = "Shit happens!!!:("
    expected_text = test_text[-2]
    app.create_comment(test_text)
    # Verifications
    comments_elements = app.get_comments()
    assert comments_elements[0].text == expected_text
