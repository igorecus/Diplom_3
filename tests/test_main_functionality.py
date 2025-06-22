import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


class TestMainFunctionality:

    @allure.title("Проверка перехода по клику на «Конструктор»")
    def test_transition_to_constructor_page_by_clicking_constructor_button(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.page_loading_wait()
        main_page.click_constructor_button()

        actual_text = main_page.get_page_constructor_name()
        expected_text = "Соберите бургер"
        assert actual_text == expected_text, f"Ожидался текст '{expected_text}', а получен '{actual_text}'"

    @allure.title("Проверка перехода по клику на «Лента заказов»")
    def test_transition_to_feed_page_by_clicking_order_feed_button(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.open_main_page()
        main_page.page_loading_wait()
        main_page.click_order_feed_button()

        actual_text = order_feed_page.get_order_feed_page_name()
        expected_text = "Лента заказов"
        assert actual_text == expected_text, f"Ожидался текст '{expected_text}', а получен '{actual_text}'"

    @allure.title("Проверка появления всплывающего окна с деталями при клике на ингредиент")
    def test_presense_ingredient_details_popup_after_clicking_on_ingredient_icon(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.page_loading_wait()
        main_page.click_ingredient_bun_button()

        actual_text = main_page.get_details_window_name()
        expected_text = "Детали ингредиента"
        assert actual_text == expected_text, f"Ожидался текст '{expected_text}', а получен '{actual_text}'"

        main_page.click_close_up_ingredient_details_popup_button()
        main_page.click_ingredient_sauce_button()

        actual_text2 = main_page.get_details_window_name()
        expected_text2 = "Детали ингредиента"
        assert actual_text2 == expected_text2, f"Ожидался текст '{expected_text2}', а получен '{actual_text2}'"

        main_page.click_close_up_ingredient_details_popup_button()
        main_page.scroll_to_magnolia_patty()
        main_page.click_ingredient_topping_button()

        actual_text3 = main_page.get_details_window_name()
        expected_text3 = "Детали ингредиента"
        assert actual_text3 == expected_text3, f"Ожидался текст '{expected_text3}', а получен '{actual_text3}'"

    @allure.title("Проверка закрытия всплывающего окна кликом по крестику")
    def test_close_ingredient_modal_by_cross_button(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.page_loading_wait()
        main_page.click_ingredient_bun_button()

        title = main_page.get_details_window_name()
        assert title == "Детали ингредиента", "Модальное окно не открылось"

        main_page.click_close_up_ingredient_details_popup_button()
        main_page.wait_for_ingredient_modal_to_disappear()

    @allure.title('Проверка увеличения каунтера ингридиента при добавлении в заказ')
    def test_counter_increase_when_adding_ingredient_into_basket(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.page_loading_wait()

        initial_count = main_page.get_ingredient_counter_count()
        assert initial_count == 0, f"Ожидалось значение 0, а получено '{initial_count}'"

        main_page.put_ingredient_into_basket()

        updated_count = main_page.get_ingredient_counter_count()
        assert updated_count > 0, f"Ожидалось значение > 0, а получено '{updated_count}'"

    @allure.title('Проверка возможности оформления заказа залогиненым пользователем')
    def test_the_possibility_of_placing_an_order_by_a_logged_in_user(self, driver, login):
        main_page = MainPage(driver)

        main_page.page_loading_wait()
        main_page.put_ingredient_into_basket()
        main_page.click_order_button()
        main_page.page_loading_wait()

        text = main_page.get_order_has_already_been_prepared_message_text()
        assert text == "Ваш заказ начали готовить", "Кто-то сегодня будет голодный;-)"
