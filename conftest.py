import pytest
from selenium import webdriver
from pages.auth_page import AuthPage
from pages.main_page import MainPage
from data import Credentials


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def login(driver):
    """
    Фикстура для авторизации пользователя.
    """
    driver.delete_all_cookies()
    main_page = MainPage(driver)
    auth_page = AuthPage(driver)

    main_page.open_main_page()
    main_page.page_loading_wait()
    main_page.click_personal_account_button()
    auth_page.auth(Credentials.email,Credentials.password)

    return driver

