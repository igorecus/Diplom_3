from selenium.webdriver.common.by import By

class OrderFeedPageLocators:

    ORDER_FEED_TEXT = (By.XPATH, "//h1[text()='Лента заказов']")
    FIRST_ORDER_FROM_LIST = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')]")
    FIRST_ORDER_NUMBER = (By.XPATH, "//p[contains(@class, 'text_type_digits-default')]")
    POPUP_WINDOW_WITH_DETAILS = (By.XPATH, "//div[contains(@class, 'Modal_orderBox')]")

