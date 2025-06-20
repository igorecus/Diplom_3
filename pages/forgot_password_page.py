import allure
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage
from urls import Urls


class ForgotPasswordPage(BasePage):
    @allure.step("Открыть страницу восстановления пароля")
    def open_forgot_password_page(self):
        self.get(Urls.FORGOT_PASSWORD_PAGE)

    @allure.step("Проверяем имя открытой страницы")
    def check_forgot_password_page_name(self):
        actual_text = self.get_text_on_element(ForgotPasswordPageLocators.RESTORE_PAGE_NAME)
        return actual_text

    @allure.step('Ввод почты: {email}')
    def email_input(self, email):
        self.send_keys_to_input(ForgotPasswordPageLocators.EMAIL_FIELD, email)

    @allure.step("Кликаем по кнопке «Восстановить»")
    def click_restore_button(self):
        self.click_on_element(ForgotPasswordPageLocators.RESTORE_BUTTON)
