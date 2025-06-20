import allure
from pages.login_page import LoginPage
from helper import generate_registration_data
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage
from pages.main_page import MainPage


class TestRestorePassword:

    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_the_transition_to_the_forgot_password_page_by_clicking_on_the_restore_password_link(self, driver):
        login_page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)
        main_page = MainPage(driver)

        login_page.open_login_page()
        main_page.page_loading_wait()
        login_page.click_restore_password_link()
        actual_page_title = forgot_password_page.check_forgot_password_page_name()

        assert actual_page_title == "Восстановление пароля", f"Ожидали 'Восстановление пароля', получили '{actual_page_title}'"


    @allure.title('Проверка ввода почты и клик по кнопке «Восстановить»')
    def test_email_input_and_clicking_on_the_restore_button(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        main_page = MainPage(driver)
        reset_password_page = ResetPasswordPage(driver)

        email, _ = generate_registration_data()

        forgot_password_page.open_forgot_password_page()
        main_page.page_loading_wait()
        forgot_password_page.check_forgot_password_page_name()
        forgot_password_page.email_input(email)
        forgot_password_page.click_restore_button()

        actual_page_url = reset_password_page.check_opened_page_name_is_reset_password()
        assert '/reset-password' in actual_page_url


    @allure.title('Проверка, что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_show_hide_password_button_make_password_field_active(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)
        main_page = MainPage(driver)
        email, password = generate_registration_data()

        forgot_password_page.open_forgot_password_page()
        main_page.page_loading_wait()
        forgot_password_page.check_forgot_password_page_name()
        forgot_password_page.email_input(email)
        forgot_password_page.click_restore_button()

        main_page.page_loading_wait()
        reset_password_page.check_password_field_by_default()
        reset_password_page.password_input(password)

        input_type_before = reset_password_page.get_password_input_type_before_password_field_be_activated()
        assert input_type_before == "password", "Ожидалось, что до клика поле будет иметь type='password'"

        reset_password_page.click_show_password_icon()

        active_field = reset_password_page.check_password_field_is_active()
        assert active_field is not None, "Поле пароля не стало активным после клика на иконку"

        input_type_after = reset_password_page.get_password_input_type_after_password_field_was_activated()
        assert input_type_after == "text", "Ожидалось, что после клика поле будет иметь type='text'"
