import allure
import time
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step('Поиск элемента')
    def find_element_with_wait(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Кликабельность элемента')
    def check_element_is_clickable(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))
        return self.find_element_with_wait(locator)

    @allure.step('Ожидание для закрытия модального окна')
    def wait_for_modal_closed(self, locator):
        try:
            self.wait.until(EC.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            print("Модальное окно не закрылось")
            return False

    @allure.step('Клик по элементу')
    def click_to_element(self, locator):
        self._close_all_modals()

        for attempt in range(3):
            try:
                element = self.check_element_is_clickable(locator)
                element.click()
                return True
            except (TimeoutException, StaleElementReferenceException) as e:
                if attempt == 2:
                    try:
                        element = self.driver.find_element(*locator)
                        self.driver.execute_script("arguments[0].click();", element)
                        return True
                    except Exception as js_e:
                        print(f"Ошибка при клике через JavaScript: {js_e}")
                        return False
                time.sleep(0.5)

    @allure.step('Добавление текста в элемент')
    def add_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.clear()
        element.send_keys(text)

    @allure.step('Получение текста из элемента')
    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        text = element.text
        if not text:
            text = self.driver.execute_script("return arguments[0].textContent;", element)
        return text.strip()

    @allure.step('Прокрутить к элементу')
    def scroll_into_view(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        time.sleep(0.5)

    @allure.step('Отображение элемента')
    def element_is_displayed(self, locator):
        try:
            return self.find_element_with_wait(locator).is_displayed()
        except TimeoutException:
            return False

    @allure.step('Закрыть все модальные окна')
    def _close_all_modals(self):
        try:
            modals = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'Modal_modal')]")
            if modals:
                self.driver.execute_script("""
                    var modals = document.querySelectorAll('[class*="Modal_modal"]');
                    modals.forEach(function(modal) {
                        modal.remove();
                    });
                """)
                time.sleep(0.5)
        except Exception as e:
            print(f"Ошибка при закрытии модальных окон: {e}")