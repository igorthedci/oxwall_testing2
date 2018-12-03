from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Open browser and Oxwall site, driver settings
driver = webdriver.Chrome()
driver.get('http://127.0.0.1/oxwall/')
driver.implicitly_wait(5)
driver.maximize_window()

# Login
driver.find_element(By.XPATH, '//*[contains(@id,"console_item")]/span[1]').click()
login = driver.find_element(By.NAME, 'identity')
login.click()
login.send_keys('admin')
passw = driver.find_element(By.NAME, 'password')
passw.click()
passw.send_keys('pass')
driver.find_element(By.XPATH, "//div[@class='ow_right']").click()

# Wait until login finishing
time.sleep(5)

# Write some text to Newsfeed form and send it
newsfeed = driver.find_element_by_name("status")
newsfeed.click()
newsfeed.clear()
newsfeed.click()

test_text = "Shit happens!!!:("
newsfeed.send_keys(test_text)
send_button = driver.find_element_by_name("save")
send_button.click()

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
