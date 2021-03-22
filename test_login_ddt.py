import time
import allure
import pytest
import self as self
from selenium import webdriver
from allure_commons.types import AttachmentType
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_DDT_Login:

    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/testdata.xlsx"
    logger = LogGen.loggen()

    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self, setup):
        self.logger.info("####### Testcase_002_DDT_test #########")
        self.logger.info('****** Verifying test_login() ********')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, "data")
        print("Number of Rows: "+str(self.rows))

        lst_status = []

        for r in range(2, self.rows+1):
            self.user = XLUtils.readData(self.path, 'data', r, 1)
            self.password = XLUtils.readData(self.path, 'data', r, 2)
            self.exp = XLUtils.readData(self.path, 'data', r, 3)

            print(self.user+" "+self.password+" "+self.exp, end=" ")

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(2)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Passed":
                    self.logger.info("***** Login Passed *****")
                    self.lp.clickLogout()
                    lst_status.append("Passed")
                elif self.exp == "Failed":
                    allure.attach(self.driver.get_screenshot_as_png(), name="screenShot", attachment_type=AttachmentType.PNG)
                    self.logger.error("*** Login Failed ****")
                    self.lp.clickLogout()
                    lst_status.append("Failed")
            elif act_title != exp_title:
                if self.exp == "Passed":
                    allure.attach(self.driver.get_screenshot_as_png(), name="Pass Match", attachment_type=AttachmentType.PNG)
                    self.logger.info("***** Login Failed *****")
                    lst_status.append("Failed")
                elif self.exp == "Failed":
                    self.logger.error("**** Passed ****")
                    lst_status.append("Passed")

        if "Failed" not in lst_status:
            self.logger.info("**** Login DDT Test Passed... ****")
            self.driver.close()
            assert True
        else:
            allure.attach(self.driver.get_scrrenshot_as_png(), name="Total Failed", attachment_type=AttachmentType.PNG)
            self.logger.info("**** Login DDT Test Failed... ****")
            self.driver.close()
            assert False

        self.logger.error('****** End of Login Test ********')
        self.logger.error('****** Completed TC_Login_DDT_002_Testcase ********')
























