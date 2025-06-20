from selenium.webdriver.common.by import By

class PersonalAccountPageLocators:

    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    ORDERS_HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")
    LOGOUT_LINK = (By.XPATH, "//button[text()='Выход']")

    LAST_ORDER_NUMBER = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')][last()]//p[contains(@class, 'text_type_digits-default')]")