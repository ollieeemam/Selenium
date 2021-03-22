
class LoginPage:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    rememberme_checkbox_id = "RememberMe"
    login_button_xpath = "//button[@type='submit' and @class='button-1 login-button']"
    link_logout_xpath = "//a[@href='/logout' and text()='Logout']"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def check_Rememberme(self):
        self.driver.find_element_by_id(self.rememberme_checkbox_id).click()

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_xpath(self.link_logout_xpath).click()



























