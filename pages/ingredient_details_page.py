import allure
from locators import Locators
from pages.base_page import BasePage


class IngredientDetailsPage(BasePage):
    @allure.step('Проверить видимость модального окна ингредиента')
    def is_visible(self):
        return self.element_is_displayed(Locators.INGREDIENT_MODAL)

    @allure.step('Закрыть модальное окно ингредиента')
    def close(self):
        self.click_to_element(Locators.MODAL_CLOSE_BUTTON)
        self.wait_element_invisible(Locators.INGREDIENT_MODAL)
        return self