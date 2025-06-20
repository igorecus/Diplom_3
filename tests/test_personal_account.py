import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage


class TestPersonalAccount:

    @allure.title('Проверка перехода по клику на «Личный кабинет»')
    def test_personal_account_transition(self, driver, login):
        personal_account_page = PersonalAccountPage(driver)
        main_page = MainPage(driver)

        main_page.page_loading_wait()
        main_page.click_personal_account_button()

        actual_page_url = personal_account_page.check_opened_page_name_is_personal_account()
        assert '/account/profile' in actual_page_url

    @allure.title('Проверка перехода в раздел «История заказов»')
    def test_history_orders_transition(self, driver, login):
        personal_account_page = PersonalAccountPage(driver)
        main_page = MainPage(driver)

        main_page.page_loading_wait()
        main_page.click_personal_account_button()
        main_page.page_loading_wait()
        personal_account_page.open_orders_history()

        actual_page_url = personal_account_page.check_opened_page_name_is_order_history()
        assert '/account/order-history' in actual_page_url

    @allure.title('Проверка выхода из аккаунта')
    def test_log_out(self, driver, login):
        personal_account_page = PersonalAccountPage(driver)
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        main_page.page_loading_wait()
        main_page.click_personal_account_button()

        actual_page_url = personal_account_page.check_opened_page_name_is_personal_account()
        assert '/account/profile' in actual_page_url

        main_page.page_loading_wait()
        personal_account_page.logout()

        actual_login_page_url = login_page.check_opened_page_name_is_login()
        assert '/login' in actual_login_page_url
