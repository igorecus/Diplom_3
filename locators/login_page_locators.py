from selenium.webdriver.common.by import By

class LoginPageLocators:

    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Восстановить пароль")
    RESTORE_PAGE_NAME = (By.XPATH, "//h2[text() = 'Восстановление пароля']")
    LOGIN_EMAIL_FIELD = (By.XPATH, "//label[text() = 'Email']//following-sibling::input")
    LOGIN_PASSWORD_FIELD = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    LOG_IN_BUTTON = (By.XPATH, "//button[text()='Войти']")

