import allure
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)

    @allure.step('Проверить и закрыть все открытые модальные окна')
    def close_all_modals(self):
        try:
            overlay = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")
            if overlay:
                close_buttons = self.driver.find_elements(By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
                if close_buttons:
                    self.driver.execute_script("arguments[0].click();", close_buttons[0])
                    self.wait.until(EC.invisibility_of_element_located(
                        (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")))
                else:
                    self.driver.execute_script("""
                        var overlays = document.querySelectorAll('div[class*="Modal_modal_overlay"]');
                        overlays.forEach(function(overlay) {
                            overlay.remove();
                        });
                    """)
                return self.close_all_modals()
            return True
        except Exception as e:
            print(f"Ошибка при закрытии модальных окон: {str(e)}")
            try:
                self.driver.execute_script("""
                    var modals = document.querySelectorAll('[class*="Modal_modal"]');
                    modals.forEach(function(modal) {
                        modal.remove();
                    });
                """)
                return True
            except:
                print("Не удалось закрыть модальные окна даже через JavaScript")
                return False

    @allure.step('Найти элемент и дождаться его видимости')
    def find_element_with_wait(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Найти элемент и дождаться его кликабельности')
    def find_clickable_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step('Проверить, что элемент отображается')
    def element_is_displayed(self, locator):
        try:
            return self.find_element_with_wait(locator).is_displayed()
        except TimeoutException:
            return False

    @allure.step('Проверить, что элемент кликабелен')
    def element_is_clickable(self, locator):
        try:
            self.wait.until(EC.element_to_be_clickable(locator))
            return True
        except TimeoutException:
            return False

    @allure.step('Кликнуть по элементу')
    def click_to_element(self, locator):
        self.close_all_modals()

        attempts = 3
        for attempt in range(attempts):
            try:
                element = self.find_clickable_element(locator)
                element.click()
                return True
            except (TimeoutException, StaleElementReferenceException) as e:
                if attempt == attempts - 1:
                    try:
                        element = self.driver.find_element(*locator)
                        self.driver.execute_script("arguments[0].click();", element)
                        return True
                    except Exception as js_e:
                        print(f"Не удалось кликнуть по элементу: {str(js_e)}")
                        return False

    @allure.step('Ввести текст в элемент')
    def type_text(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.clear()
        element.send_keys(text)

    @allure.step('Получить текст элемента')
    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        text = element.text
        if not text:
            text = self.driver.execute_script("return arguments[0].textContent;", element)
        return text.strip()

    @allure.step('Прокрутить страницу к элементу')
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center'});", element)

    @allure.step('Ждать исчезновения элемента')
    def wait_element_invisible(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step('Закрыть модальное окно, если оно открыто')
    def dismiss_modal(self):
        return self.close_all_modals()

    @allure.step('Перетащить элемент')
    def drag_and_drop(self, source_locator, target_locator):
        source = self.find_element_with_wait(source_locator)
        target = self.find_element_with_wait(target_locator)

        try:
            self.actions.drag_and_drop(source, target).perform()
            return True
        except Exception as e:
            print(f"Стандартный drag_and_drop не сработал: {str(e)}")

            try:
                js_drag_drop = """
                function simulateDragDrop(sourceNode, destinationNode) {
                    var EVENT_TYPES = {
                        DRAG_END: 'dragend',
                        DRAG_START: 'dragstart',
                        DROP: 'drop'
                    };

                    function createCustomEvent(type) {
                        var event = new CustomEvent("CustomEvent");
                        event.initCustomEvent(type, true, true, null);
                        event.dataTransfer = {
                            data: {},
                            setData: function(type, val) { this.data[type] = val; },
                            getData: function(type) { return this.data[type]; }
                        };
                        return event;
                    }

                    function dispatchEvent(node, type, event) {
                        if (node.dispatchEvent) {
                            return node.dispatchEvent(event);
                        }
                        if (node.fireEvent) {
                            return node.fireEvent("on" + type, event);
                        }
                    }

                    var event = createCustomEvent(EVENT_TYPES.DRAG_START);
                    dispatchEvent(sourceNode, EVENT_TYPES.DRAG_START, event);

                    var dropEvent = createCustomEvent(EVENT_TYPES.DROP);
                    dropEvent.dataTransfer = event.dataTransfer;
                    dispatchEvent(destinationNode, EVENT_TYPES.DROP, dropEvent);

                    var dragEndEvent = createCustomEvent(EVENT_TYPES.DRAG_END);
                    dragEndEvent.dataTransfer = event.dataTransfer;
                    dispatchEvent(sourceNode, EVENT_TYPES.DRAG_END, dragEndEvent);
                }
                simulateDragDrop(arguments[0], arguments[1]);
                """
                self.driver.execute_script(js_drag_drop, source, target)
                return True
            except Exception as js_e:
                print(f"JavaScript drag_and_drop не сработал: {str(js_e)}")
                return False

    @allure.step('Проверить URL страницы')
    def check_url_contains(self, substring):
        return substring in self.driver.current_url

    @allure.step('Открыть страницу по URL')
    def open_url(self, url):
        try:
            self.driver.get(url)
            self.close_all_modals()
            return self
        except TimeoutException as e:
            print(f"Таймаут при загрузке страницы {url}: {e}")
            return self