from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C://Users/ollie/Drivers/chromedriver.exe")
url = "https://www.kuwaitairways.com/en"
driver.implicitly_wait(5)

driver.get(url)
driver.maximize_window()
time.sleep(2)
print("Title: "+driver.title)

driver.find_element_by_xpath("//a[@id='signup']").click()
time.sleep(3)

inputBoxes = driver.find_elements_by_css_selector("input")
print(len(inputBoxes))

className = driver.find_elements_by_xpath("//span[@class='select2-selection select2-selection--single focus-within']")
print(len(className))

tags = driver.find_element_by_tag_name('a')


time.sleep(2)
driver.close()
driver.quit()






# form-control text-field focus-within






