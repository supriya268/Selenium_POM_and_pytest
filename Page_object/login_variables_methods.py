# from  selenium import webdriver
# import time

class Test_Login_Home():

    login_mail_xpath = "//*[@id='txtUsername']"
    login_Password_xpath = "//*[@id='txtPassword']"
    login_button_xpath = "//*[@id='btnLogin']"

    def __init__(self,driver):
        self.driver= driver

    def test_setUsername(self,UserName):
        self.driver.find_element_by_xpath(self.login_mail_xpath).send_keys(UserName)

    def test_setPassword(self, Password):
        self.driver.find_element_by_xpath(self.login_Password_xpath).send_keys(Password)

    def test_LogInButton(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()






    # def LogOut(self):
    #     self.driver.find_element_by_xpath(self.logout_xpath).click()
    #
