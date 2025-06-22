import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class AuthPage(BasePage):

    @allure.step("Авторизоваться")
    def auth(self, email, password):
        self.send_keys_to_input(LoginPageLocators.LOGIN_EMAIL_FIELD, email)
        self.send_keys_to_input(LoginPageLocators.LOGIN_PASSWORD_FIELD, password)
        self.click_on_element(LoginPageLocators.LOG_IN_BUTTON)