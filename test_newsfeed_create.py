from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get('http://127.0.0.1/oxwall/')
time.sleep(5)
driver.find_element(By.XPATH, '//*[contains(@id,"console_item")]/span[1]').click()
login = driver.find_element(By.NAME, 'identity')
login.click()
login.send_keys('admin')
passw = driver.find_element(By.NAME, 'password')
passw.click()
passw.send_keys('pass')
driver.find_element(By.XPATH, "//div[@class='ow_right']").click()

time.sleep(5)

newsfeed = driver.find_element_by_name("status")
newsfeed.click()
newsfeed.clear()
newsfeed.click()

test_text = "Shit happens!!!:("
expected_text = test_text[-2]

newsfeed.send_keys(test_text)
send_button = driver.find_element_by_name("save")
send_button.click()

time.sleep(2)

text_element = driver.find_elements_by_class_name("ow_newsfeed_content")

print(text_element[0].text)


assert text_element[0].text == expected_text

menu = driver.find_element(By.LINK_TEXT, 'Admin')
actions = ActionChains(driver)
actions.move_to_element(menu).perform()
driver.find_element(By.XPATH, './/a[contains(@href,"sign-out")]').click()

driver.close()
