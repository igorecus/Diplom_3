import allure
from locators.reset_password_page_locators import ResetPasswordPageLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):

    @allure.step('Проверяем URL страницы авторизации')
    def check_opened_page_name_is_reset_password(self):
        self.wait_for_url_contains('/reset-password')
        return self.driver.current_url

    @allure.step("Проверить, что поле Пароль есть и оно неактивно по умолчанию")
    def check_password_field_by_default(self):
        self.wait_for_element(ResetPasswordPageLocators.PASSWORD_FIELD_BY_DEFAULT)

    @allure.step('Ввод пароля')
    def password_input(self, password):
        self.send_keys_to_input(ResetPasswordPageLocators.PASSWORD_FIELD, password)

    @allure.step("Убедиться, что вместо текста отображаются символы (password/text)")
    def get_password_input_type_before_password_field_be_activated(self):
        element = self.wait_for_element(ResetPasswordPageLocators.PASSWORD_FIELD)
        return element.get_attribute("type")

    @allure.step("Кликаем по кнопке показать/скрыть пароль")
    def click_show_password_icon(self):
        self.click_on_element(ResetPasswordPageLocators.SHOW_OR_HIDE_PASSWORD_BUTTON)

    @allure.step("Убедиться, что в поле Пароль отображается текст (password/text)")
    def get_password_input_type_after_password_field_was_activated(self):
        element = self.wait_for_element(ResetPasswordPageLocators.PASSWORD_FIELD)
        return element.get_attribute("type")

    @allure.step("Проверить, что поле Пароль стало активным/подсвечивается")
    def check_password_field_is_active(self):
        return self.wait_for_element(ResetPasswordPageLocators.PASSWORD_FIELD_ACTIVE)
