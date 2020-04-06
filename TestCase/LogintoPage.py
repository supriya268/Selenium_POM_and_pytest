from  selenium import webdriver
import time
import pytest
import sys
sys.path.append("/home/shamanth/PycharmProjects/AUTOMATION_PROJECT1")
from Page_object.login_variables_methods import Test_Login_Home

class Test_LoginTest():

    baseUrl = "https://opensource-demo.orangehrmlive.com/"
    username="Admin"
    password="admin123"
    driver=webdriver.Chrome("/home/shamanth/PycharmProjects/AUTOMATION_PROJECT1/Drivers/chromedriver")

    @pytest.fixture()
    def setup(self):
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
    
        yield

        self.driver.close()

    def test_login(self):
        lp= Test_Login_Home(self.driver)
        lp.test_setUsername(self.username)
        lp.test_setPassword(self.password)
        lp.test_LogInButton()
        # assert self.driver.title == "OrangeHRM"
        # time.sleep(5)clear
        # self.assertEqual("Guru99 Bank Home Page", self.driver.title, "this is not the titile")
        # lp.LogOut()

