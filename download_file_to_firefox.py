from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

fireFoxProfile = webdriver.FirefoxProfile()
fireFoxProfile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain,application/pdf") # Mime type
fireFoxProfile.set_preference("browser.download.manager.showWhenStarting", False)
fireFoxProfile.set_preference("browser.download.dir", "c:/Downloadedfiles")
fireFoxProfile.set_preference("browser.download.folderList", 2)
fireFoxProfile.set_preference("pdfjs.disabled", True)


driverPath = "C://Users/ollie/eclipse-workspace/chromedriver.exe"
url = "https://demo.automationtesting.in/FileDownload.html"


driver = webdriver.Firefox(executable_path=driverPath, firefox_profile=fireFoxProfile)
driver.get(url)
driver.implicitly_wait(7)
driver.maximize_window()
time.sleep(2)

















