from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
import importlib


driver = webdriver.Chrome(executable_path="C://Users/ollie/eclipse-workspace/chromedriver.exe")
url = "https://smartours.com/new-tours/"

driver.get(url)
driver.maximize_window()
time.sleep(2)
print("Title: "+driver.title)

opentousLink = driver.find_element_by_xpath("//span[@class='ubermenu-target-title ubermenu-target-text']").is_enabled()
if opentousLink:
    driver.find_element_by_xpath("//span[@class='ubermenu-target-title ubermenu-target-text']").click()

time.sleep(2)
print("Open to US title: "+driver.title)
time.sleep(3)
driver.back()

time.sleep(2)
driver.forward()
time.sleep(2)

driver.quit()










