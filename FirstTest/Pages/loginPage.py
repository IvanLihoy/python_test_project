import time

from selenium.webdriver.common.by import By

from FirstTest.base import BasePage


class LoginPage(BasePage):

    username_textbox_class = (By.CSS_SELECTOR, "input[class = 'ng-invalid']")
    login_button_value = (By.CSS_SELECTOR, "input[value='Log in']")

    def enter_id(self, userID):
        time.sleep(2)
        self.driver.find_element_by_css_selector(LoginPage.username_textbox_class).send_keys(userID)

    def click_login(self):
        self.driver.find_element_by_css_selector(LoginPage.login_button_value).click()
