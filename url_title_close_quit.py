from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C://Users/ollie/Drivers/chromedriver.exe")
driver.get("https://www.google.com")

title = driver.title
print("Title is: "+title)

url = driver.current_url
print("Current Url: "+url)



driver.close()
driver.quit()






























