from selenium.webdriver.common.by import By


class Locators:

    MODAL_BACKDROP = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")

    AUTH_EMAIL_FIELD = (By.XPATH, "//input[@name='name']")
    AUTH_PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']")
    AUTH_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(@class,'button_button_type_primary') and text()='Войти']")
    RESTORE_ACCESS_LINK = (By.XPATH, "//a[contains(@class,'Auth_link') and normalize-space()='Восстановить пароль']")

    RESTORE_EMAIL_FIELD = (By.XPATH, "//input")
    RESTORE_SUBMIT_BTN = (By.XPATH, "//button[text()='Восстановить']")

    PASSWORD_INPUT_FIELD = (By.XPATH, "//input[@type='password']")
    VERIFICATION_CODE = (By.XPATH, "//input[@name='name']")
    SAVE_PASSWORD_BTN = (By.XPATH, "//button[text()='Сохранить']")
    PASSWORD_TOGGLE_BTN = (By.XPATH, "//div[contains(@class,'input__icon-action')]")

    PASSWORD_FIELD_ACTIVE = (By.XPATH, "//label[text()='Пароль']/parent::div[contains(@class,'input_status_active')]")
    PASSWORD_FIELD_VISIBLE = (By.XPATH, "//input[@type='text' and @name='Пароль']")
    PASSWORD_FIELD_HIDDEN = (By.XPATH, "//input[@type='password' and @name='Пароль']")

    MENU_CONSTRUCTOR = (By.XPATH, "//a[contains(@class,'AppHeader_header__link') and .//p[text()='Конструктор']]")
    MENU_PROFILE = (By.XPATH, "//a[contains(@href, '/account')]")
    MENU_FEED = (By.XPATH, "//a[contains(@class,'AppHeader_header__link') and .//p[text()='Лента Заказов']]")
    ORDERS_HISTORY_LINK = (By.XPATH, "//a[contains(text(), 'История заказов')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

    CONSTRUCTOR_AREA = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_burger__container')]")

    BUN_INGREDIENT = (By.XPATH, "//a[contains(@class, 'ingredients-item')]//p[contains(text(), 'булка')]")
    FILLING_INGREDIENT = (By.XPATH, "//a[contains(@class, 'ingredients-item')]//p[contains(text(), 'котлета')]")
    SAUCE_INGREDIENT = (By.XPATH, "//a[contains(@class, 'ingredients-item')]//p[contains(text(), 'соус')]")

    TAB_BUNS = (By.CSS_SELECTOR, ".tab_tab__1SPyG:nth-child(1)")
    TAB_SAUCES = (By.CSS_SELECTOR, ".tab_tab__1SPyG:nth-child(2)")
    TAB_FILLINGS = (By.CSS_SELECTOR, ".tab_tab__1SPyG:nth-child(3)")

    BURGER_TOP_BUN = (By.XPATH, "//div[contains(@class, 'constructor-element_pos_top')]")
    BURGER_BOTTOM_BUN = (By.XPATH, "//div[contains(@class, 'constructor-element_pos_bottom')]")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")

    INGREDIENT_COUNTER = (By.XPATH, "//p[contains(@class, 'counter_counter__num')]")

    INGREDIENT_MODAL = (By.XPATH, "//div[contains(@class,'Modal_modal__content')]/h2[text()='Детали ингредиента']")
    INGREDIENT_CLOSE = (
        By.XPATH, "//div[contains(@class,'Modal_modal__content')]//button[contains(@class,'Modal_modal__close')]")
    ING_MODAL = INGREDIENT_MODAL
    ING_CLOSE = INGREDIENT_CLOSE

    ORDER_DETAILS_MODAL = (By.XPATH, "//div[contains(@class,'Modal_modal__content')]/h2[text()='Детали заказа']")
    ORDER_ID_NUMBER = (By.CSS_SELECTOR, ".text_type_digits-large")

    ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")
    ORDER_MODAL_CONTENT = (By.XPATH,
                           "//div[contains(@class, 'Modal_modal')]//p[contains(text(), 'идентификатор заказа')] | //div[contains(@class, 'Modal_modal')]//p[contains(text(), 'Состав')]")
    ORDER_MODAL_CLOSE = (By.XPATH, '//button[contains(@class, "Modal_modal__close")]')
    ORDER_NUMBER = (By.XPATH, "//p[contains(@class, 'text_type_digits-large')]")
    ORDER_STATUS = (By.XPATH, "//p[text()='Ваш заказ начали готовить']")
    ORDER_STATUS_TEXT = (By.XPATH, "//p[text()='Ваш заказ начали готовить']")
    ORDER_WAIT_TEXT = (By.XPATH, "//p[text()='Дождитесь готовности на орбитальной станции']")

    ORDER_FEED_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]")
    ORDER_CARD = (By.XPATH, "//li[contains(@class, 'OrderFeed_orderCard')]")

    STATS_TOTAL = (By.XPATH,
                   '//p[contains(text(), "Выполнено за все время")]/following-sibling::p[contains(@class, "text_type_digits-large")]')
    STATS_TODAY = (By.XPATH,
                   '//p[contains(text(), "Выполнено за сегодня")]/following-sibling::p[contains(@class, "text_type_digits-large")]')
    IN_PROGRESS = (By.XPATH, '//p[text()="В работе:"]/following-sibling::div//p')


    HEADER_ACCOUNT = (By.XPATH, "//a[contains(@class,'AppHeader_header__link') and .//p[text()='Личный Кабинет']]")
    NAV_ACCOUNT = HEADER_ACCOUNT  # Алиас
    HISTORY_NAV = (By.XPATH, "//a[contains(text(), 'История заказов')]")
    HISTORY_LINK = HISTORY_NAV  # Алиас
    ORDER_NUMBER_CARD = (By.XPATH, "//p[contains(@class, 'text_type_digits-default')]")
    NAV_CONSTRUCTOR = (By.XPATH, "//a[contains(@class,'AppHeader_header__link') and .//p[text()='Конструктор']]")
    HEADER_CONSTRUCTOR = NAV_CONSTRUCTOR  # Алиас
    NAV_FEED = (By.XPATH, "//a[contains(@class,'AppHeader_header__link') and .//p[text()='Лента Заказов']]")
    HEADER_FEED = NAV_FEED  # Алиас


    FEED_TITLE = (By.XPATH, "//h1[text()='Лента заказов']")
    FEED_ORDERS_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]")
    FEED_FIRST_ORDER = (By.XPATH, "//li[contains(@class, 'OrderFeed_orderCard')][1]")
    FEED_TOTAL_ORDERS = (By.XPATH, '//p[contains(text(), "Выполнено за все время")]/following-sibling::p')
    FEED_TODAY_ORDERS = (By.XPATH, '//p[contains(text(), "Выполнено за сегодня")]/following-sibling::p')
    FEED_IN_PROGRESS_TITLE = (By.XPATH, '//p[text()="В работе:"]')
    FEED_IN_PROGRESS_ORDERS = (By.XPATH, '//p[text()="В работе:"]/following-sibling::ul/li')

    HISTORY_ORDER_CARD = (By.XPATH, "//li[contains(@class, 'OrderFeed_orderCard')]")
    HISTORY_ORDER_NUMBER = (By.XPATH, "//p[contains(@class, 'text_type_digits-default')]")