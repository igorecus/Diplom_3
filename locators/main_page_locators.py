from selenium.webdriver.common.by import By

class MainPageLocators:

    OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    ASSEMBLE_A_BURGER_TEXT = (By.XPATH, "//h1[text()='Соберите бургер']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    CLOSE_POPUP_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified__3V5XS')]")
    DETAILS_WINDOW_TEXT = (By.XPATH, "//h2[text()='Детали ингредиента']")
    BASKET = By.XPATH, ".//ul[contains(@class, 'BurgerConstructor_basket')]"
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_STARTED_TEXT = (By.XPATH, "//p[text()='Ваш заказ начали готовить']")
    ORDER_NUMBER_IN_MODAL = (By.XPATH, "//h2[contains(@class, 'text_type_digits-large')]")
    CLOSE_MODAL_WINDOW_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")


    FLUORESCENT_ROLL_R2_D3 = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")
    COUNTER_FLUORESCENT_ROLL = (By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]/ancestor::a//p[contains(@class, "counter_counter__num")]')
    SPICY_X_SAUCE = (By.XPATH, "//p[text()='Соус Spicy-X']")
    COUNTER_SPICY_X_SAUCE = (By.XPATH, '//p[text()="Соус Spicy-X"]/ancestor::a//p[contains(@class, "counter_counter__num")]')
    ORGANIC_MARTIAN_MAGNOLIA_PATTY = (By.XPATH, "//p[text()='Биокотлета из марсианской Магнолии']")
    COUNTER_ORGANIC_MARTIAN_MAGNOLIA_PATTY = (By.XPATH, '//p[text()="Биокотлета из марсианской Магнолии"]/ancestor::a//p[contains(@class, "counter_counter__num")]')

