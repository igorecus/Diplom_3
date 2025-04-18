import allure
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from pages.base_page import BasePage


class PersonalAccountPage(BasePage):
    @allure.step('Открыть страницу личного кабинета')
    def open_account(self):
        self.click_to_element(Locators.HEADER_ACCOUNT)
        self.wait.until(lambda d: '/account' in d.current_url)
        assert self.check_url_contains('/account'), "Не выполнен переход в личный кабинет"
        return self

    @allure.step('Открыть историю заказов')
    def open_history(self):
        self.click_to_element(Locators.HISTORY_LINK)
        self.wait.until(lambda d: '/order-history' in d.current_url)
        assert self.check_url_contains('/order-history'), "Не выполнен переход в историю заказов"
        return self

    @allure.step('Выйти из аккаунта')
    def logout(self):
        self.close_all_modals()
        logout_button = self.wait.until(
            EC.element_to_be_clickable(Locators.LOGOUT_BUTTON)
        )
        self.driver.execute_script("arguments[0].click();", logout_button)
        self.wait.until(lambda d: '/login' in d.current_url)
        assert self.check_url_contains('/login'), "Не выполнен выход из аккаунта"
        self.wait.until(
            EC.visibility_of_element_located(Locators.AUTH_SUBMIT_BUTTON)
        )
        return self

    @allure.step('Получить номер заказа из истории')
    def get_order_number_from_history(self):
        try:
            self.find_element_with_wait(Locators.HISTORY_ORDER_CARD)
            order_number_text = self.get_text_from_element(Locators.HISTORY_ORDER_NUMBER)
            if order_number_text.startswith('#'):
                order_number_text = order_number_text[1:]
            return order_number_text
        except Exception as e:
            print(f"Ошибка при получении номера заказа из истории: {str(e)}")
            return None

    @allure.step('Проверить наличие заказа в истории')
    def check_order_in_history(self, order_number):
        try:
            order_locator = (Locators.HISTORY_ORDER_NUMBER[0],
                             f"{Locators.HISTORY_ORDER_NUMBER[1]}[contains(text(), '{order_number}')]")
            return self.element_is_displayed(order_locator)
        except Exception as e:
            print(f"Ошибка при проверке заказа в истории: {str(e)}")
            return False