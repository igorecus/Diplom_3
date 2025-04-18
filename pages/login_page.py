import allure
from locators import Locators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step('Открыть страницу логина')
    def open(self):
        self.open_url("https://stellarburgers.nomoreparties.site/login")
        return self

    @allure.step('Ввести email пользователя: {email}')
    def enter_email(self, email):
        self.type_text(Locators.AUTH_EMAIL_FIELD, email)
        return self

    @allure.step('Ввести пароль пользователя')
    def enter_password(self, password):
        self.type_text(Locators.AUTH_PASSWORD_FIELD, password)
        return self

    @allure.step('Нажать кнопку входа')
    def click_login_button(self):
        self.click_to_element(Locators.AUTH_SUBMIT_BUTTON)
        return self

    @allure.step('Авторизоваться с данными: {email}')
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
        self.dismiss_modal()
        return self

    @allure.step('Перейти на страницу восстановления пароля')
    def go_to_forgot_password(self):
        self.click_to_element(Locators.RESTORE_ACCESS_LINK)
        assert self.check_url_contains('forgot-password'), "Не выполнен переход на страницу восстановления пароля"
        return self

    @allure.step('Проверить успешность авторизации')
    def is_logged_in(self):
        try:
            return self.element_is_displayed(Locators.PLACE_ORDER_BUTTON)
        except:
            return False