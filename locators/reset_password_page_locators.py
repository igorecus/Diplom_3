from selenium.webdriver.common.by import By

class ResetPasswordPageLocators:

    PASSWORD_FIELD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    SHOW_OR_HIDE_PASSWORD_BUTTON = (By.XPATH, "//label[text() = 'Пароль']/following-sibling::div")
    PASSWORD_FIELD_BY_DEFAULT = (By.XPATH, "//label[text() = 'Пароль']/parent::div[contains(@class, 'input_size_default')]")
    PASSWORD_FIELD_ACTIVE = (By.XPATH, "//label[text() = 'Пароль']/parent::div[contains(@class, 'input_status_active')]")

