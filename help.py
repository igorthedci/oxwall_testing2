from selenium import webdriver
import random
driver = webdriver.Chrome()


def complete_profile():
    if "COMPLETE YOUR PROFILE" in driver.find_element_by_tag_name("body").text:
        pass
