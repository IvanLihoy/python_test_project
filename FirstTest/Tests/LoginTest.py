import time

from FirstTest.Pages.loginPage import LoginPage
from FirstTest.chrome_config import TestTemplate


class TestLogin(TestTemplate):

    def test_valid_login(self):
        self.login = LoginPage(self.driver)
        self.login.enter_id("30")
        self.login.click_login()
        time.sleep(5)
