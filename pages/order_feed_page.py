import allure
from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators


class OrderFeedPage(BasePage):
    @allure.step("Получаем название страницы ленты заказов")
    def get_order_feed_page_name(self):
        self.wait_for_attribute(OrderFeedPageLocators.ORDER_FEED_TEXT, "textContent", "Лента заказов")
        return self.find_element(OrderFeedPageLocators.ORDER_FEED_TEXT).text

    @allure.step("Кликаем по первому заказу списка ленты")
    def click_on_the_order_from_the_feed(self):
        self.click_on_element(OrderFeedPageLocators.FIRST_ORDER_FROM_LIST)

    @allure.step("Находим открытое окно с деталями заказа")
    def find_opened_popup_window_with_details(self):
        return self.find_element(OrderFeedPageLocators.POPUP_WINDOW_WITH_DETAILS)

    @allure.step("Получаем номер заказа из ленты заказов без символа # и ведущих нулей")
    def get_order_number_from_order_feed(self):
        order_text = self.get_text_on_element(OrderFeedPageLocators.FIRST_ORDER_NUMBER)
        return order_text.replace("#", "").lstrip("0")

    @allure.step("Получить значение счетчика «Выполнено за все время»")
    def get_main_counter_count(self):
        text = self.get_text_on_element(OrderFeedPageLocators.MAIN_COUNTER_VALUE)
        return int(text)

    @allure.step("Получить значение счетчика «Выполнено за сегодня»")
    def get_today_counter_count(self):
        text = self.get_text_on_element(OrderFeedPageLocators.TODAY_COUNTER_VALUE)
        return int(text)

    @allure.step("Получить номер заказа «В работе»")
    def get_in_process_order_number(self):
        in_process_number = self.get_text_on_element(OrderFeedPageLocators.IN_PROCESS_ORDER)
        return in_process_number.lstrip("0")

    @allure.step("Ожидаем появления номера заказа в разделе 'В работе'")
    def wait_for_order_number_in_progress(self, order_number):
        self.wait_for_text_on_element(OrderFeedPageLocators.IN_PROCESS_ORDER, order_number)




