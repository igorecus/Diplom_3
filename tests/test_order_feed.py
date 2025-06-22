import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.personal_account_page import PersonalAccountPage


class TestOrderFeed:

    @allure.title("Проверка открытия всплывающего окна с деталями при клике на заказ")
    def test_the_opening_of_a_popup_window_with_details_when_clicking_on_an_order(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.open_main_page()
        main_page.page_loading_wait()
        main_page.click_order_feed_button()
        order_feed_page.click_on_the_order_from_the_feed()

        popup_window = order_feed_page.find_opened_popup_window_with_details()
        assert popup_window.is_displayed()

    @allure.title("Проверка отображения заказов пользователя из раздела «История заказов» на странице «Лента заказов»")
    def test_displaying_user_orders_from_the_order_history_section_on_the_order_feed_page(self, driver, login):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        personal_account_page = PersonalAccountPage(driver)

        main_page.page_loading_wait()
        main_page.put_ingredient_into_basket()
        main_page.click_order_button()
        main_page.page_loading_wait()
        order_number_from_modal = main_page.get_order_number_from_modal()
        main_page.click_close_modal_window_button()
        main_page.click_order_feed_button()
        first_order_number = order_feed_page.get_order_number_from_order_feed()

        assert order_number_from_modal == first_order_number, \
            f"Номер заказа из модального окна ({order_number_from_modal}) не одинаков с нашим заказом в ленте заказов ({first_order_number})"

        main_page.click_personal_account_button()
        main_page.page_loading_wait()
        personal_account_page.open_orders_history()
        main_page.page_loading_wait()
        personal_account_page.scroll_to_last_order_number()

        last_order_number = personal_account_page.get_order_number_from_orders_history()

        assert first_order_number == last_order_number, \
            f"Номер заказа из ленты заказов ({first_order_number}) не найден в истории заказов"

    @allure.title("Проверка увеличения счётчика Выполнено за всё время при создании нового заказа")
    def test_the_increment_of_the_completed_in_all_time_counter_when_creating_a_new_order(self, driver, login):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.page_loading_wait()
        main_page.click_order_feed_button()
        main_page.page_loading_wait()
        current_counter_value = order_feed_page.get_main_counter_count()

        main_page.click_constructor_button()
        main_page.page_loading_wait()
        main_page.put_ingredient_into_basket()
        main_page.click_order_button()
        main_page.page_loading_wait()
        main_page.click_close_modal_window_button()
        main_page.click_order_feed_button()
        counter_value_after_an_order = order_feed_page.get_main_counter_count()

        assert counter_value_after_an_order > current_counter_value, "Значение счетчика после заказа должно стать больше значения до заказа"

    @allure.title("Проверка увеличения счётчика Выполнено за сегодня при создании нового заказа")
    def test_the_increment_of_the_completed_today_counter_when_creating_a_new_order(self, driver, login):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.page_loading_wait()
        main_page.click_order_feed_button()
        main_page.page_loading_wait()
        current_counter_value = order_feed_page.get_today_counter_count()

        main_page.click_constructor_button()
        main_page.page_loading_wait()
        main_page.put_ingredient_into_basket()
        main_page.click_order_button()
        main_page.page_loading_wait()
        main_page.click_close_modal_window_button()
        main_page.click_order_feed_button()
        counter_value_after_an_order = order_feed_page.get_today_counter_count()

        assert counter_value_after_an_order > current_counter_value, "Значение счетчика после заказа должно стать больше значения до заказа"

    @allure.title("Проверка отображения номера заказа в разделе В работе после его оформления")
    def test_order_number_display_in_progress_after_registration(self, driver, login):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.page_loading_wait()
        main_page.put_ingredient_into_basket()
        main_page.click_order_button()
        main_page.page_loading_wait()
        order_number_from_modal = main_page.get_order_number_from_modal()
        main_page.click_close_modal_window_button()
        main_page.click_order_feed_button()
        order_feed_page.wait_for_order_number_in_progress(order_number_from_modal)
        in_progress_number = order_feed_page.get_in_process_order_number()

        assert order_number_from_modal == in_progress_number, \
            f"Номер заказа из модального окна ({order_number_from_modal}) не одинаков с нашим заказом в разделе В работе ({in_progress_number})"




