from selenium import webdriver
# import time
# import unittest
# from FirstTest.Pages.loginPage import LoginPage
from FirstTest.base import BasePage

from selenium.webdriver.common.keys import Keys

# File = "D:\PycharmProjects\TCW\\batman-dc-comics.jpg"


# class LoginTest(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls):
    #     cls.driver = webdriver.Chrome("D:/PycharmProjects/TCW/chromedriver.exe")
    #     cls.driver.implicitly_wait(10)
    #     cls.driver.maximize_window()

    # def test_login_valid(self):
    #     # driver = self.driver
    #     # driver.get("http://qa.tcw.local")
    #     login = LoginPage(self.driver)
    #     login.enter_id("30")
    #     login.click_login()

        # self.driver.find_element_by_css_selector("input.ng-invalid").send_keys(30)
        # self.driver.find_element_by_css_selector("[value='Log in']").click()

        # time.sleep(2)

        # "self.driver.find_element_by_css_selector(".profile-img").is_displayed()"
        # print("user is logged in")

    # def test_uploadCompanyLogo(self):
    #     self.driver.find_element_by_xpath(
    #         "/html/body/app-root/div/div[2]/app-private/div/app-top-bar/div[1]/div[2]/ul/li[3]/a/div[2]").click()
    #     self.driver.find_element_by_xpath(
    #         "/html/body/app-root/div/div[2]/app-private/div/app-top-bar/div[2]/ul/li[2]/a/span[2]").click()
    #     time.sleep(2)
    #     self.driver.find_element_by_xpath("(//button[@class='edit-btn ng-star-inserted'])[1]").click()
    #     # driver.find_element_by_xpath("(//div[@class = 'user_profile__picture'])[1]").click()
    #     self.driver.find_element_by_xpath(
    #         "/html/body/app-root/div/div[2]/app-private/div/div/app-profile/div/p-tabview/div/div/app-company-profile/div/app-company/div/form/div[1]/div/div[1]/app-profile-picture/div/div/img").click()
    #     time.sleep(2)
    #     # driver.find_element_by_css_selector("input[type = 'file']").click()
    #     self.driver.find_element_by_css_selector("input[type = 'file']").send_keys(File)
    #     self.driver.find_element_by_xpath("//span[contains(text(), 'Save')]").click()

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.close()
    #     cls.driver.quit()
    #     print("Test Completed")


# if __name__ == '__main__':
#     unittest.main()
