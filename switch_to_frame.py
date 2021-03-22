from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

driverPath = "C://Users/ollie/Drivers/chromedriver.exe"
url = "https:////seleniumhq.github.io/selenium/docs/api/java/index.html"


driver = webdriver.Chrome(executable_path="C://Users/ollie/eclipse-workspace/chromedriver.exe")
driver.get(url)
driver.implicitly_wait(7)
driver.maximize_window()
time.sleep(2)
frame = driver.find_element_by_xpath("//a[@href='index.html?overview-summary.html']")
print("1. Frame is displayed? "+str(frame.is_displayed()))
print("2. Title of Home page: "+str(driver.title))

if frame.is_displayed() and frame.is_enabled():
    driver.find_element_by_xpath("//a[@href='index.html?overview-summary.html']").click()
else:
    print("Sorry! No frame present.")

time.sleep(1)
print("3. Frame title: "+str(driver.title))



driver.switch_to.frame("packageListFrame")
driver.find_element_by_xpath("//a[@href='org/openqa/selenium/devtools/package-frame.html']").click()
print("4 First Frame title: "+str(driver.title))
time.sleep(3)

driver.back()
driver.switch_to.default_content()
driver.switch_to.frame("packageFrame")
driver.find_element_by_xpath("//a[@href='org/openqa/selenium/devtools/v86/accessibility/Accessibility.html']").click()
print("5 Second Frame title: "+str(driver.title))
time.sleep(3)

driver.back()
driver.switch_to.default_content()
driver.switch_to.frame("classFrame")
driver.find_element_by_xpath("//a[@href='org/openqa/selenium/cli/package-summary.html']").click()
print("5 Second Frame title: "+str(driver.title))
time.sleep(3)
















driver.close()
driver.quit()





























