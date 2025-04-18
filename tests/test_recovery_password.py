import pytest
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators


@pytest.mark.usefixtures('driver')
class TestRecoveryPassword:

    @allure.title('Проверка перехода на страницу восстановления пароля')
    def test_navigate_to_forgot_password(self, driver):
        try:
            driver.get("https://stellarburgers.nomoreparties.site/login")

            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(Locators.RESTORE_ACCESS_LINK)
            ).click()

            WebDriverWait(driver, 10).until(
                lambda d: 'forgot-password' in d.current_url
            )
            assert 'forgot-password' in driver.current_url
        except Exception as e:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="navigate_to_forgot_password_error",
                attachment_type=allure.attachment_type.PNG
            )
            pytest.fail(f"Ошибка при переходе на страницу восстановления пароля: {e}")

    @allure.title('Проверка ввода email на странице восстановления пароля')
    def test_submit_email(self, driver, generate_user_credentials):
        """Проверка ввода email и клика по кнопке 'Восстановить' на странице восстановления пароля"""
        try:
            email, _, _ = generate_user_credentials

            driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

            email_field = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(Locators.RESTORE_EMAIL_FIELD)
            )
            email_field.clear()
            email_field.send_keys(email)

            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(Locators.RESTORE_SUBMIT_BTN)
            ).click()

            WebDriverWait(driver, 10).until(
                lambda d: 'reset-password' in d.current_url
            )
            assert 'reset-password' in driver.current_url, "URL не содержит reset-password"

            save_button = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(Locators.SAVE_PASSWORD_BTN)
            )
            assert save_button.is_displayed(), "Кнопка 'Сохранить' не отображается"
        except Exception as e:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="submit_email_error",
                attachment_type=allure.attachment_type.PNG
            )
            pytest.fail(f"Ошибка при отправке email для восстановления: {e}")

    @allure.title('Проверка работы кнопки показать/скрыть пароль')
    def test_show_hide_password_focus(self, driver, generate_user_credentials):
        try:
            email, _, _ = generate_user_credentials
            driver.get("https://stellarburgers.nomoreparties.site/login")
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(Locators.RESTORE_ACCESS_LINK)
            ).click()

            email_field = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(Locators.RESTORE_EMAIL_FIELD)
            )
            email_field.clear()
            email_field.send_keys(email)

            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(Locators.RESTORE_SUBMIT_BTN)
            ).click()

            WebDriverWait(driver, 10).until(
                lambda d: 'reset-password' in d.current_url
            )

            driver.execute_script("""
                var elements = document.querySelectorAll('.Modal_modal__overlay__x2ZCr, [class*="Modal_modal_overlay"], [class*="Modal_modal"]');
                if (elements.length > 0) {
                    elements.forEach(el => el.remove());
                }
            """)

            password_field = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(Locators.PASSWORD_INPUT_FIELD)
            )
            assert password_field.is_displayed(), "Поле ввода пароля не отображается"

            is_active_before = driver.execute_script("""
                var field = arguments[0];
                return (document.activeElement === field);
            """, password_field)

            toggle_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(Locators.PASSWORD_TOGGLE_BTN)
            )

            driver.execute_script("arguments[0].click();", toggle_button)

            active_field = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(Locators.PASSWORD_FIELD_ACTIVE)
            )
            assert active_field.is_displayed(), "Поле пароля не стало активным после клика по иконке 'глаз'"

        except Exception as e:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="show_hide_password_error",
                attachment_type=allure.attachment_type.PNG
            )
            pytest.fail(f"Ошибка при проверке переключения видимости пароля: {e}")
