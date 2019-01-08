from page_objects.main_page import MainPage


# TODO: parametrize to users, add non-admin users
def test_login_using_page_object(driver, user):
    main_page = MainPage(driver)
    sign_in_page = main_page.sign_in_click()
    assert sign_in_page.is_this_page()
    sign_in_page.input_username(user.username)
    sign_in_page.input_password(user.password)
    dashboard_page = sign_in_page.submit_form()
    assert dashboard_page.is_this_page()
    assert dashboard_page.is_logged_in()
    assert dashboard_page.is_logged_in_as(user)
