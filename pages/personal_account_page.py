import allure
from pages.base_page import BasePage
from locators.personal_account_page_locators import PersonalAccountPageLocators


class PersonalAccountPage(BasePage):

    @allure.step('Проверяем URL страницы «Личный кабинет»')
    def check_opened_page_name_is_personal_account(self):
        self.wait_for_url_contains('/account/profile')
        return self.driver.current_url

    @allure.step('Открыть историю заказов')
    def open_orders_history(self):
        self.click_on_element(PersonalAccountPageLocators.ORDERS_HISTORY_LINK)

    @allure.step("Скроллим до последнего заказа")
    def scroll_to_last_order_number(self):
        self.scroll_to_element(PersonalAccountPageLocators.LAST_ORDER_NUMBER)

    @allure.step("Получаем номер заказа из истории заказов без символа # и ведущих нулей")
    def get_order_number_from_orders_history(self):
        order_text = self.get_text_on_element(PersonalAccountPageLocators.LAST_ORDER_NUMBER)
        return order_text.replace("#", "").lstrip("0")

    @allure.step('Проверяем URL страницы «История заказов»')
    def check_opened_page_name_is_order_history(self):
        self.wait_for_url_contains('/account/order-history')
        return self.driver.current_url

    @allure.step('Выйти из аккаунта')
    def logout(self):
        self.click_on_element(PersonalAccountPageLocators.LOGOUT_LINK)

