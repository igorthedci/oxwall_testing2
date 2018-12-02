import pytest
from oxwall_site import Oxwall


@pytest.fixture()
def app():
    app = Oxwall()
    yield app
    app.close()


@pytest.fixture()
def login_user(app):
    app.login('admin', 'pass')
    yield
    app.logout('admin')


# Фикстуры для теста написанного низкоуровневым кодом
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects import locators
from selenium.webdriver import ActionChains


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    driver.maximize_window()
    driver.get('http://127.0.0.1/oxwall/')
    yield driver
    driver.quit()


@pytest.fixture()
def login_low_level(driver):
    username = "admin"
    password = "pass"
    driver.find_element(*locators.SIGN_IN_MENU).click()
    login = driver.find_element(*locators.LOGIN_FIELD)
    login.click()
    login.send_keys(username)
    passw = driver.find_element(*locators.PASS_FIELD)
    passw.click()
    passw.send_keys(password)
    driver.find_element(*locators.SIGN_IN_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(locators.LOGIN_BACKGROUND))
    yield
    # Logout
    menu = driver.find_element(By.LINK_TEXT, username.title())
    ActionChains(driver).move_to_element(menu).perform()
    driver.find_element(By.XPATH, './/a[contains(@href,"sign-out")]').click()

