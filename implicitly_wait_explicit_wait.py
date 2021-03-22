from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C://Users/ollie/Drivers/chromedriver.exe")
url = "https://www.tripadvisor.com/Attraction_Review-g60763-d17585889-Reviews-New_Tours-New_York_City_New_York.html"
driver.implicitly_wait(5)

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


print(isSelected)
driver.find_element_by_xpath("//span[text()='United Airlines']").click()

time.sleep(2)

driver.find_element_by_xpath("//button[text()='Find flights' and @type='button']").click()
time.sleep(3)
# print("Best Flight title: "+driver.title)

wait = WebDriverWait(driver, 10)

clickRadio = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Nonstop']")))
clickRadio.click()

time.sleep(3)


driver.quit()








