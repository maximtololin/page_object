from pages.base_page import BasePage
from pages.locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Current URL does not contain 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = "testpassword123"
        # находим элементы для полей ввода email, пароля и кнопки регистрации
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL).send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD).send_keys(password)
        password_confirm_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM).send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()

