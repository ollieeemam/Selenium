import time

from allure_commons.types import AttachmentType
from selenium import webdriver
import allure
import pytest


@allure.severity(allure.severity_level.NORMAL)
class TestHRMOrange:
    def test_logo(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        status = self.driver.find_element_by_xpath("//*[@id='divLogo']/img").is_displayed()
        if status == True:
            allure.attach(self.driver.get_screenshot_as_png(), name="Orange Title", attachment_type=AttachmentType.PNG)
            assert True
            print("1. HRM Logo is Displayed.")
            self.driver.close()
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="Orange title Failed",
                          attachment_type=AttachmentType.PNG)
            assert False
            print("1. HRM Logo is not Displayed.")
            self.driver.close()

    @allure.severity(allure.severity_level.MINOR)
    def test_listEmaployee(self):
        pytest.skip('Skipping this test, later will be implemented.')

    @allure.severity(allure.severity_level.CRITICAL)
    def test_Login(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys("Admin")
        self.driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("admin123")
        self.driver.find_element_by_xpath("//input[@id='btnLogin']").click()
        actual_title = self.driver.title

        if actual_title == "OrangeHRM":
            allure.attach(self.driver.get_screenshot_as_png(), name='Orange HRM', attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert True
            print("2. Orange hrm Title match.")
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="testLoginScreen",
                          attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False
            print("2. Orange hrm Title does not match.")

