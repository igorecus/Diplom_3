import allure
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    @allure.step('Открыть страницу ленты заказов')
    def open_feed(self):
        self.close_all_modals()
        feed_button = self.driver.find_element(*Locators.HEADER_FEED)
        self.driver.execute_script("arguments[0].click();", feed_button)
        assert self.check_url_contains('/feed'), "Не выполнен переход на страницу ленты заказов"
        try:
            self.find_element_with_wait(Locators.FEED_TITLE)
        except:
            self.driver.refresh()
            self.close_all_modals()
            self.find_element_with_wait(Locators.FEED_TITLE)
        return self

    @allure.step('Проверить наличие заказов в ленте')
    def is_order_list_not_empty(self):
        try:
            time.sleep(2)
            feed_list = self.driver.find_element(*Locators.FEED_ORDERS_LIST)
            order_cards = feed_list.find_elements(By.XPATH, ".//li")
            return len(order_cards) > 0
        except (TimeoutException, NoSuchElementException):
            return False

    @allure.step('Открыть детали заказа')
    def open_order(self, order_number=None):
        self.close_all_modals()
        if order_number:
            try:
                order_locator = (By.XPATH, f"//p[contains(text(), '{order_number}')]/ancestor::li")
                order_element = self.driver.find_element(*order_locator)
                self.driver.execute_script("arguments[0].click();", order_element)
            except Exception as e:
                print(f"Ошибка при открытии заказа с номером {order_number}: {str(e)}")
                return False
        else:
            try:
                time.sleep(2)
                first_order = self.driver.find_element(*Locators.FEED_FIRST_ORDER)
                self.driver.execute_script("arguments[0].click();", first_order)
            except Exception as e:
                print(f"Ошибка при открытии первого заказа: {str(e)}")
                return False
        time.sleep(1)
        return self.is_order_modal()

    @allure.step('Проверить, открыто ли модальное окно заказа')
    def is_order_modal(self):
        try:
            return self.element_is_displayed(Locators.ORDER_MODAL)
        except:
            return False

    @allure.step('Получить общее количество заказов')
    def get_total(self):
        try:
            self.scroll_to_element(Locators.FEED_TOTAL_ORDERS)
            time.sleep(1)
            total_element = self.driver.find_element(*Locators.FEED_TOTAL_ORDERS)
            total_text = total_element.text.strip()
            return int(total_text.replace(" ", ""))
        except (TimeoutException, ValueError, NoSuchElementException) as e:
            print(f"Ошибка при получении общего количества заказов: {str(e)}")
            return 0

    @allure.step('Получить количество заказов за сегодня')
    def get_today(self):
        try:
            self.scroll_to_element(Locators.FEED_TODAY_ORDERS)
            time.sleep(1)
            today_element = self.driver.find_element(*Locators.FEED_TODAY_ORDERS)
            today_text = today_element.text.strip()
            return int(today_text.replace(" ", ""))
        except (TimeoutException, ValueError, NoSuchElementException) as e:
            print(f"Ошибка при получении количества заказов за сегодня: {str(e)}")
            return 0

    @allure.step('Проверить заказ в разделе "В работе"')
    def check_order_in_progress(self, order_number):
        try:
            self.find_element_with_wait(Locators.FEED_IN_PROGRESS_TITLE)
            time.sleep(2)
            in_progress_elements = self.driver.find_elements(*Locators.FEED_IN_PROGRESS_ORDERS)
            in_progress_numbers = [elem.text.strip() for elem in in_progress_elements]
            for number in in_progress_numbers:
                if order_number in number or number in order_number:
                    return True
            return False
        except Exception as e:
            print(f"Ошибка при проверке заказа в разделе 'В работе': {str(e)}")
            return False

    @allure.step('Получить номера заказов в разделе "В работе"')
    def get_in_progress_orders(self):
        try:
            self.scroll_to_element(Locators.FEED_IN_PROGRESS_TITLE)
            time.sleep(2)
            in_progress_elements = self.driver.find_elements(*Locators.FEED_IN_PROGRESS_ORDERS)
            return [elem.text.strip() for elem in in_progress_elements]
        except Exception as e:
            print(f"Ошибка при получении заказов в разделе 'В работе': {str(e)}")
            return []

    @allure.step('Проверить наличие заказа в ленте')
    def check_order_in_feed(self, order_number):
        try:
            time.sleep(2)
            order_locator = (By.XPATH, f"//p[contains(text(), '{order_number}')]/ancestor::li")
            orders = self.driver.find_elements(*order_locator)
            return len(orders) > 0
        except Exception as e:
            print(f"Ошибка при проверке заказа в ленте: {str(e)}")
            return False