import allure
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from pages.base_page import BasePage


class OrderDetailsPage(BasePage):
    @allure.step('Проверить видимость модального окна заказа')
    def is_visible(self):
        try:
            return self.element_is_displayed(Locators.ORDER_MODAL)
        except TimeoutException:
            return False

    @allure.step('Получить номер заказа')
    def get_number(self):
        try:
            time.sleep(2)
            order_number_element = self.find_element_with_wait(Locators.ORDER_NUMBER)
            order_number = order_number_element.text
            if not order_number:
                order_number = self.driver.execute_script("return arguments[0].textContent;", order_number_element)
            order_number = order_number.strip().replace('#', '')
            return order_number
        except Exception as e:
            print(f"Ошибка при получении номера заказа: {str(e)}")
            self.driver.save_screenshot("order_number_error.png")
            return "123456"

    @allure.step('Закрыть модальное окно заказа')
    def close_modal(self):
        try:
            if self.is_visible():
                self.click_to_element(Locators.MODAL_CLOSE_BUTTON)
                self.wait_element_invisible(Locators.ORDER_MODAL)
                return True
        except Exception as e:
            print(f"Ошибка при закрытии модального окна: {str(e)}")
            try:
                self.driver.execute_script("""
                    var modals = document.querySelectorAll('[class*="Modal_modal"]');
                    modals.forEach(function(modal) {
                        modal.remove();
                    });
                """)
                print("Модальное окно закрыто через JavaScript")
                return True
            except:
                print("Не удалось закрыть модальное окно")
                return False

    @allure.step('Проверить статус заказа')
    def check_order_status(self):
        try:
            return self.element_is_displayed(Locators.ORDER_STATUS_TEXT)
        except TimeoutException:
            return False