from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import locator
import time

# Open browser and Oxwall site, driver settings
driver = webdriver.Chrome()
driver.get('http://127.0.0.1/oxwall/')
driver.implicitly_wait(5)
driver.maximize_window()
wait = WebDriverWait(driver, 5)


def login_as(username, password):
    # Login
    driver.find_element(*locator.SIGN_IN_MENU).click()
    login = driver.find_element(*locator.LOGIN_FIELD)
    login.click()
    login.send_keys(username)
    passw = driver.find_element(*locator.PASS_FIELD)
    passw.click()
    passw.send_keys(password)
    driver.find_element(*locator.SIGN_IN_BUTTON).click()
    # Wait until grey background disappeared
    wait.until(EC.invisibility_of_element_located(locator.LOGIN_BACKGROUND))


login_as('admin', 'pass')

# Write some text to Newsfeed form and send it
newsfeed = driver.find_element_by_name("status")
newsfeed.click()
newsfeed.clear()
newsfeed.click()

test_text = "Shit happens!!!:("
newsfeed.send_keys(test_text)
send_button = driver.find_element_by_name("save")
send_button.click()

# Wait until new status appear
time.sleep(2)

# Verification that new status with this text appeared
text_element = driver.find_elements_by_class_name("ow_newsfeed_content")
expected_text = test_text[-2]
assert text_element[0].text == expected_text

#Logout
menu = driver.find_element(By.LINK_TEXT, 'Admin')
actions = ActionChains(driver)
actions.move_to_element(menu).perform()
driver.find_element(By.XPATH, './/a[contains(@href,"sign-out")]').click()

# Close browser
driver.close()
