import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import locator


@pytest.fixture()
def driver():
    # Open browser and Oxwall site, driver settings
    driver = webdriver.Chrome()
    driver.get('http://127.0.0.1/oxwall/')
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    # Close browser
    driver.quit()


@pytest.fixture()
def user():
    return {"username": "admin", "password": "pass"}


@pytest.fixture()
def login(driver, user):
    # Login
    driver.find_element(*locator.SIGN_IN_MENU).click()
    login = driver.find_element(*locator.LOGIN_FIELD)
    login.click()
    login.send_keys(user["username"])
    passw = driver.find_element(*locator.PASS_FIELD)
    passw.click()
    passw.send_keys(user["password"])
    driver.find_element(*locator.SIGN_IN_BUTTON).click()
    # Wait until grey background disappeared
    wait = WebDriverWait(driver, 5)
    wait.until(EC.invisibility_of_element_located(locator.LOGIN_BACKGROUND))


@pytest.fixture()
def logout(user):
    yield             # Because we need to do it after test
    # Logout
    menu = driver.find_element(By.LINK_TEXT, user.title())
    actions = ActionChains(driver)
    actions.move_to_element(menu).perform()
    driver.find_element(By.XPATH, './/a[contains(@href,"sign-out")]').click()
