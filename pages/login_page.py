from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        current_url = self.browser.current_url
        assert "login" in current_url, f"URL does not contain 'login'. Current URL: {current_url}"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_FIELD)
        assert self.is_element_present(*LoginPageLocators.LOGIN_USER_FIELD)

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL_FIELD)
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_FIELD)
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASSWORD_CONFIRMATION_FIELD)