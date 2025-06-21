import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from urls import Urls

class MainPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.get(Urls.MAIN_PAGE)

    @allure.step("Ждем загрузки страницы")
    def page_loading_wait(self):
        self.wait_for_element_hide(MainPageLocators.OVERLAY)

    @allure.step("Кликаем по кнопке «Конструктор»")
    def click_constructor_button(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Получаем название страницы конструктора")
    def get_page_constructor_name(self):
        self.wait_for_attribute(MainPageLocators.ASSEMBLE_A_BURGER_TEXT, "textContent", "Соберите бургер")
        return self.find_element(MainPageLocators.ASSEMBLE_A_BURGER_TEXT).text

    @allure.step("Кликаем по кнопке входа в личный кабинет")
    def click_personal_account_button(self):
        self.click_on_element(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Кликаем по кнопке «Лента Заказов»")
    def click_order_feed_button(self):
        self.click_on_element(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Кликаем по ингридиенту - булке")
    def click_ingredient_bun_button(self):
        self.click_on_element(MainPageLocators.FLUORESCENT_ROLL_R2_D3)

    @allure.step("Кликаем по ингридиенту - соусу")
    def click_ingredient_sauce_button(self):
        self.click_on_element(MainPageLocators.SPICY_X_SAUCE)

    @allure.step("Скроллим до биокотлеты из марсианской Магнолии")
    def scroll_to_magnolia_patty(self):
        self.scroll_to_element(MainPageLocators.ORGANIC_MARTIAN_MAGNOLIA_PATTY)

    @allure.step("Кликаем по ингридиенту - начинке")
    def click_ingredient_topping_button(self):
        self.click_on_element(MainPageLocators.ORGANIC_MARTIAN_MAGNOLIA_PATTY)

    @allure.step("Закрываем всплывающее окно кликом по крестику")
    def click_close_up_ingredient_details_popup_button(self):
        self.click_on_element(MainPageLocators.CLOSE_POPUP_BUTTON)

    @allure.step("Получаем название окна с деталями ингридиента")
    def get_details_window_name(self):
        self.wait_for_attribute(MainPageLocators.DETAILS_WINDOW_TEXT, "textContent", "Детали ингредиента")
        return self.find_element(MainPageLocators.DETAILS_WINDOW_TEXT).text

    @allure.step("Ожидаем, что окно с деталями ингредиента закрылось")
    def wait_for_ingredient_modal_to_disappear(self):
        self.wait_for_element_hide(MainPageLocators.DETAILS_WINDOW_TEXT)

    @allure.step("Добавить ингридиент в заказ")
    def put_ingredient_into_basket(self):
        ingredient = self.wait_for_element(MainPageLocators.FLUORESCENT_ROLL_R2_D3)
        basket = self.wait_for_element(MainPageLocators.BASKET)
        self.drag_and_drop_element(ingredient, basket)

    @allure.step("Получить значение счетчика ингредиента")
    def get_ingredient_counter_count(self):
        text = self.get_text_on_element(MainPageLocators.COUNTER_FLUORESCENT_ROLL)
        return int(text)

    @allure.step("Кликаем по кнопке «Оформить заказ»")
    def click_order_button(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON)

    @allure.step("Получить номер заказа из модального окна")
    def get_order_number_from_modal(self):
        return self.get_text_on_element(MainPageLocators.ORDER_NUMBER_IN_MODAL)

    @allure.step("Получить текст сообщения 'Ваш заказ начали готовить'")
    def get_order_has_already_been_prepared_message_text(self):
        self.wait_for_element(MainPageLocators.ORDER_STARTED_TEXT)
        return self.get_text_on_element(MainPageLocators.ORDER_STARTED_TEXT)

    @allure.step("Кликаем по кнопке закрытия модального окна")
    def click_close_modal_window_button(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.CLOSE_MODAL_WINDOW_BUTTON, timeout=15)
        self.click_on_element(MainPageLocators.CLOSE_MODAL_WINDOW_BUTTON)



