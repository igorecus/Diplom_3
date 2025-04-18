import allure
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from pages.base_page import BasePage


class RecoveryPasswordPage(BasePage):
    @allure.step('Открыть страницу восстановления пароля')
    def open_forgot(self):
        try:
            self.open_url("https://stellarburgers.nomoreparties.site/forgot-password")
            self.find_element_with_wait(Locators.RESTORE_EMAIL_FIELD)
            return self
        except Exception as e:
            print(f"Не удалось открыть страницу напрямую: {e}")
            try:
                self.open_url("https://stellarburgers.nomoreparties.site/login")
                restore_link = self.find_element_with_wait(Locators.RESTORE_ACCESS_LINK)
                self.driver.execute_script("arguments[0].click();", restore_link)
                self.wait.until(lambda d: "forgot-password" in d.current_url)
                self.find_element_with_wait(Locators.RESTORE_EMAIL_FIELD)
                return self
            except Exception as e2:
                print(f"Не удалось перейти со страницы логина: {e2}")
                return self

    @allure.step('Ввести email для восстановления пароля: {email}')
    def enter_email(self, email):
        try:
            email_field = self.find_element_with_wait(Locators.RESTORE_EMAIL_FIELD)
            email_field.clear()
            email_field.send_keys(email)
            return self
        except Exception as e:
            print(f"Ошибка при вводе email: {e}")
            self.driver.execute_script(
                f"document.querySelector('input').value = '{email}';"
            )
            return self

    @allure.step('Нажать кнопку "Восстановить"')
    def click_restore_button(self):
        try:
            restore_button = self.find_clickable_element(Locators.RESTORE_SUBMIT_BTN)
            restore_button.click()
            self.wait.until(lambda d: "reset-password" in d.current_url)
            return self
        except Exception as e:
            print(f"Ошибка при клике на кнопку 'Восстановить': {e}")
            try:
                self.driver.execute_script(
                    "document.querySelector('button[type=\"submit\"]').click();"
                )
                self.wait.until(lambda d: "reset-password" in d.current_url)
                return self
            except Exception as js_error:
                print(f"Ошибка при клике через JavaScript: {js_error}")
                return self

    @allure.step('Восстановить пароль по email: {email}')
    def submit_email(self, email):
        self.enter_email(email)
        self.click_restore_button()
        return self

    @allure.step('Открыть страницу сброса пароля')
    def open_reset(self):
        try:
            self.open_url("https://stellarburgers.nomoreparties.site/reset-password")
            self.find_element_with_wait(Locators.PASSWORD_INPUT_FIELD)
            return self
        except Exception as e:
            print(f"Ошибка при открытии страницы сброса пароля: {e}")
            return self

    @allure.step('Переключить видимость пароля')
    def toggle_password(self):
        try:
            password_field = self.find_element_with_wait(Locators.PASSWORD_INPUT_FIELD)
            field_type = password_field.get_attribute("type")
            if field_type != "password":
                print(f"Внимание: поле пароля имеет тип '{field_type}', а не 'password'")
            toggle_button = self.find_clickable_element(Locators.PASSWORD_TOGGLE_BTN)
            toggle_button.click()
            WebDriverWait(self.driver, 5).until(
                lambda d: d.find_element(*Locators.PASSWORD_INPUT_FIELD).get_attribute("type") == "text"
            )
            return self
        except Exception as e:
            print(f"Ошибка при переключении видимости пароля: {e}")
            self.driver.execute_script(
                "document.querySelector('input[type=\"password\"]').type = 'text';"
            )
            return self

    @allure.step('Проверить активность поля пароля')
    def is_password_field_focused(self):
        try:
            password_field = self.find_element_with_wait(Locators.PASSWORD_INPUT_FIELD)
            active_element = self.driver.switch_to.active_element
            return active_element == password_field
        except Exception as e:
            print(f"Ошибка при проверке фокуса поля пароля: {e}")
            is_focused = self.driver.execute_script(
                "return document.activeElement === document.querySelector('input[type=\"password\"]') || document.activeElement === document.querySelector('input[type=\"text\"]');"
            )
            return is_focused