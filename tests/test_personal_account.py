import pytest
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage


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
        """Проверка выхода из аккаунта"""
        try:
            driver.execute_script("""
                var modals = document.querySelectorAll('[class*="Modal_modal"]');
                if (modals.length > 0) {
                    modals.forEach(function(modal) {
                        modal.remove();
                    });
                }
            """)

            account_page = PersonalAccountPage(driver)
            account_page.open_account()

            WebDriverWait(driver, 10).until(
                lambda d: '/account' in d.current_url
            )
            assert '/account' in driver.current_url, "Не удалось перейти в личный кабинет"

            logout_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(Locators.LOGOUT_BUTTON)
            )

            driver.execute_script("arguments[0].click();", logout_button)

            WebDriverWait(driver, 10).until(
                lambda d: '/login' in d.current_url
            )

            assert '/login' in driver.current_url, "Не выполнен выход из аккаунта"

            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(Locators.AUTH_SUBMIT_BUTTON)
            )

            login_page = LoginPage(driver)
            assert login_page.element_is_displayed(Locators.AUTH_SUBMIT_BUTTON), "Кнопка 'Войти' не отображается"

        except Exception as e:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="logout_error_screenshot",
                attachment_type=allure.attachment_type.PNG
            )
            pytest.fail(f"Ошибка при выходе из аккаунта: {e}")