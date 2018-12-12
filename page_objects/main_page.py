from page_objects.internal_page import InternalPage


class MainPage(InternalPage):
    pass

    # TODO Add all elements and actions that you have in Main Page


if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1/oxwall")
    main_page = MainPage(driver)
    main_page.sign_in_menu.click()
