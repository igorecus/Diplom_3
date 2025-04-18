import pytest
import allure
from pages.constructor_page import ConstructorPage
from pages.ingredient_details_page import IngredientDetailsPage
from pages.order_details_page import OrderDetailsPage
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage


@pytest.mark.usefixtures('driver')
class TestMainFunctionality:

    @allure.title('Проверка перехода на страницу конструктора')
    def test_navigation_to_constructor(self, driver, login):
        constructor_page = ConstructorPage(driver)
        constructor_page.go_to_constructor()
        assert '/#/' in driver.current_url

    @allure.title('Проверка открытия модального окна с деталями ингредиента')
    def test_ingredient_modal(self, driver, login):
        constructor_page = ConstructorPage(driver).open()
        constructor_page.open_ingredient()

        ingredient_details = IngredientDetailsPage(driver)
        assert ingredient_details.is_visible()

        ingredient_details.close()

    @allure.title('Проверка увеличения счетчика ингредиентов')
    def test_counter_increase(self, driver, login):
        constructor_page = ConstructorPage(driver).open()

        constructor_page.select_buns()
        before = constructor_page.get_counter()

        constructor_page.open_ingredient()

        after = constructor_page.get_counter()

        assert after > before

    @allure.title('Проверка оформления заказа авторизованным пользователем')
    def test_place_order(self, driver, login):
        constructor_page = ConstructorPage(driver).open()

        constructor_page.select_buns()
        constructor_page.add_ingredient()

        assert constructor_page.has_bun()

        constructor_page.place_order()

        order_details = OrderDetailsPage(driver)
        assert order_details.is_visible()


@pytest.mark.usefixtures('driver')
class TestPersonalAccount:

    @allure.title('Проверка перехода в личный кабинет')
    def test_account_navigation(self, driver, login):
        account_page = PersonalAccountPage(driver)
        account_page.open_account()
        assert '/account' in driver.current_url

    @allure.title('Проверка перехода в историю заказов')
    def test_history_navigation(self, driver, login):
        account_page = PersonalAccountPage(driver)
        account_page.open_account().open_history()
        assert '/order-history' in driver.current_url

    @allure.title('Проверка выхода из аккаунта')
    def test_logout(self, driver, login):
        account_page = PersonalAccountPage(driver)
        account_page.open_account().logout()

        login_page = LoginPage(driver)
        assert login_page.element_is_displayed(login_page.AUTH_SUBMIT_BUTTON)