import pytest
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.common.exceptions import TimeoutException
from faker import Faker
import allure

faker = Faker()

BASE_URL = "https://stellarburgers.nomoreparties.site"
USER_REGISTER_URL = f"{BASE_URL}/api/auth/register"
USER_LOGIN_URL = f"{BASE_URL}/api/auth/login"
USER_DELETE_URL = f"{BASE_URL}/api/auth/user"
ORDER_CREATE_URL = f"{BASE_URL}/api/orders"


@pytest.fixture(params=[webdriver.Firefox, webdriver.Chrome], ids=['firefox', 'chrome'], scope="function")
def driver(request):
    driver_class = request.param
    if driver_class == webdriver.Chrome:
        options = ChromeOptions()
        options.add_argument('--incognito')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-extensions')
        options.page_load_strategy = 'normal'
        driver = webdriver.Chrome(options=options)
    elif driver_class == webdriver.Firefox:
        firefox_options = FirefoxOptions()
        profile = FirefoxProfile()
        profile.set_preference("browser.privatebrowsing.autostart", True)
        firefox_options.profile = profile
        driver = webdriver.Firefox(options=firefox_options)

    driver.maximize_window()

    driver.set_page_load_timeout(45)

    try:
        driver.get(BASE_URL)
    except TimeoutException:
        print("Предупреждение: Таймаут при загрузке начальной страницы")

    yield driver

    try:
        driver.quit()
    except Exception as e:
        print(f"Ошибка при закрытии браузера: {e}")


@pytest.fixture
def generate_user_credentials():
    email = faker.email()
    password = faker.password(length=10, special_chars=True)
    name = faker.user_name()
    return email, password, name


@pytest.fixture
@allure.title('Создание и удаление пользователя с рандомными данными')
def create_new_user_and_delete():
    unique_suffix = faker.random_int(min=1000, max=9999)
    payload_cred = {
        'email': f'test_{unique_suffix}_{faker.email()}',
        'password': faker.password(length=10, special_chars=True),
        'name': faker.user_name()
    }

    response = requests.post(USER_REGISTER_URL, json=payload_cred)
    assert response.status_code == 200, f"Ошибка создания пользователя: {response.text}"
    response_body = response.json()
    assert response_body.get('success'), f"Не удалось создать пользователя: {response_body}"

    yield payload_cred, response_body

    access_token = response_body['accessToken']
    requests.delete(USER_DELETE_URL, headers={'Authorization': access_token})

@pytest.fixture
@allure.title('Авторизация пользователя через API + токен')
def login(driver, create_new_user_and_delete):
    user_data, response_data = create_new_user_and_delete
    access_token = response_data['accessToken']
    refresh_token = response_data['refreshToken']
    driver.execute_script("window.localStorage.clear();")

    driver.execute_script(f'window.localStorage.setItem("accessToken", "{access_token}");')
    driver.execute_script(f'window.localStorage.setItem("refreshToken", "{refresh_token}");')

    driver.refresh()
    driver.execute_script("""
        var modals = document.querySelectorAll('[class*="Modal_modal"]');
        modals.forEach(function(modal) {
            modal.remove();
        });
    """)

    return user_data

@pytest.fixture
@allure.title('Фикстура создает пользователя и заказ через API')
def create_user_and_order():
    unique_suffix = faker.random_int(min=1000, max=9999)
    user_data = {
        'email': f'test_{unique_suffix}_{faker.email()}',
        'password': faker.password(length=10, special_chars=True),
        'name': faker.user_name()
    }

    register_response = requests.post(USER_REGISTER_URL, json=user_data)
    assert register_response.status_code == 200, f"Ошибка создания пользователя: {register_response.text}"
    register_data = register_response.json()

    access_token = register_data['accessToken']

    order_data = {
        'ingredients': [
            '61c0c5a71d1f82001bdaaa73',
            '61c0c5a71d1f82001bdaaa6c',
            '61c0c5a71d1f82001bdaaa76',
            '61c0c5a71d1f82001bdaaa79'
        ]
    }

    order_response = requests.post(
        ORDER_CREATE_URL,
        json=order_data,
        headers={'Authorization': access_token}
    )

    assert order_response.status_code == 200, f"Ошибка создания заказа: {order_response.text}"
    order_result = order_response.json()

    yield user_data, register_data, order_result

    requests.delete(USER_DELETE_URL, headers={'Authorization': access_token})