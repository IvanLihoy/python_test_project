
from FirstTest.Pages.loginPage import LoginPage
from FirstTest.ChromeConfig import TestTemplate


class TestLogin(TestTemplate):

    def test_valid_login(self):
        login = LoginPage(self.driver)
        login.enter_id("30")
        login.click_login()
