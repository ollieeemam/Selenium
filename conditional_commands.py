from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C://Users/ollie/Drivers/chromedriver.exe")
url = "https://www.tripadvisor.com/Attraction_Review-g60763-d17585889-Reviews-New_Tours-New_York_City_New_York.html"

driver.get(url)
driver.maximize_window()
time.sleep(2)
print("Title: "+driver.title)

isdisplaed = driver.find_element_by_xpath("//a[@href='/Flights-g60763-New_York_City_New_York-Cheap_Discount_Airfares.html']").is_displayed()
isEnable = driver.find_element_by_xpath("//a[@href='/Flights-g60763-New_York_City_New_York-Cheap_Discount_Airfares.html']").is_enabled()
# if isdisplaed and isEnable:
#     driver.find_element_by_xpath("//a[@href='/Flights-g60763-New_York_City_New_York-Cheap_Discount_Airfares.html' and @id='global-nav-flights']").click()

driver.find_element_by_xpath("//a[@href='/Flights-g60763-New_York_City_New_York-Cheap_Discount_Airfares.html' and @id='global-nav-flights']").click()

time.sleep(2)
print("Flight title: "+driver.title)
isSelected = driver.find_element_by_xpath("//span[text()='United Airlines']").is_selected()
# isSelected = driver.find_element_by_xpath("//input[@value='KAYAK|00a43f58-7ae7-4d55-a06d-e6b94d4ffe70.1382' and @type='checkbox' and @id='KAYAK|00a43f58-7ae7-4d55-a06d-e6b94d4ffe70.1382']").is_selected()

print(isSelected)
driver.find_element_by_xpath("//span[text()='United Airlines']").click()

time.sleep(2)

driver.quit()








