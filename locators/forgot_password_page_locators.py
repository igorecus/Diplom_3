from selenium.webdriver.common.by import By

class ForgotPasswordPageLocators:

    RESTORE_PAGE_NAME = (By.XPATH, "//h2[text() = 'Восстановление пароля']")
    EMAIL_FIELD = (By.XPATH, "//label[text() = 'Email']//following-sibling::input")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")

