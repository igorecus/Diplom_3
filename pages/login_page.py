import allure
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from urls import Urls

class LoginPage(BasePage):

    @allure.step("Открыть страницу")
    def open_login_page(self):
        self.get(Urls.LOGIN_PAGE)

    @allure.step('Проверяем URL страницы авторизации')
    def check_opened_page_name_is_login(self):
        self.wait_for_url_contains('/login')
        return self.driver.current_url

    @allure.step('Ввод почты: {email}')
    def login_email_input(self, email):
        self.send_keys_to_input(LoginPageLocators.LOGIN_EMAIL_FIELD, email)

    @allure.step('Ввод пароля')
    def login_password_input(self, password):
        self.send_keys_to_input(LoginPageLocators.LOGIN_PASSWORD_FIELD, password)

    @allure.step("Кликаем по кнопке «Войти»")
    def click_log_in_button(self):
        self.click_on_element(LoginPageLocators.LOG_IN_BUTTON)

    @allure.step("Кликаем по ссылке «Восстановить пароль»")
    def click_restore_password_link(self):
        self.click_on_element(LoginPageLocators.FORGOT_PASSWORD_LINK)
