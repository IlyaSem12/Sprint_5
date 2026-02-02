from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
from config import *
from helpers import *


class TestRegistrationUser:
    
    def test_registration_page_success_registration_user_redirect_main_page(self, browser, open_registration_form):
        """Тест проверяет переход на главную страницу после регистрации"""
        email = generate_email()
        email_imput = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(EMAIL_INPUT))
        email_imput.send_keys(email)
        password_imput = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(PASSWORD_INPUT))
        password_imput.send_keys(PASSWORD)
        repeat_password_imput = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(REPEAT_PASSWORD_INPUT))
        repeat_password_imput.send_keys(PASSWORD)
        browser.find_element(*REGISTRATION_SUBMIT_BUTTON).click()
        assert BASE_URL in browser.current_url, 'Редирект на главную страницу не был произведен'

    def test_registration_page_success_registration_is_displayed_user_avatar(self, browser, open_registration_form):
        """Тест проверяет что пользователь зарегистрирован и в правом верхнем углу около кнопки «Разместить объявление» отображается аватар пользователя"""
        email = generate_email()
        email_imput = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(EMAIL_INPUT))
        email_imput.send_keys(email)
        password_imput = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(PASSWORD_INPUT))
        password_imput.send_keys(PASSWORD)
        repeat_password_imput = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(REPEAT_PASSWORD_INPUT))
        repeat_password_imput.send_keys(PASSWORD)
        browser.find_element(*REGISTRATION_SUBMIT_BUTTON).click()
        assert WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(AVATAR_BUTTON)).is_displayed() == True, 'Отсутствует аватар пользователя'
    
    def test_registration_page_success_registration_is_displayed_user_name(self, browser, open_registration_form):
        """Тест проверяет что пользователь зарегистрирован и в правом верхнем углу около кнопки «Разместить объявление» отображается имя пользователя 'User.'"""
        email = generate_email()
        email_imput = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(EMAIL_INPUT))
        email_imput.send_keys(email)
        password_imput = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(PASSWORD_INPUT))
        password_imput.send_keys(PASSWORD)
        repeat_password_imput = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(REPEAT_PASSWORD_INPUT))
        repeat_password_imput.send_keys(PASSWORD)
        browser.find_element(*REGISTRATION_SUBMIT_BUTTON ).click()
        assert WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(USERNAME_HEADER)).text == 'User.', 'Отсутствует имя пользователя'
    
    def test_registration_page_wrong_email_shows_error_message(self, browser, open_registration_form):
        """Тест проверяет при некорректном вводе email при регистрации выводится сообщение об ошибке"""
        email_imput = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(EMAIL_INPUT))
        email_imput.send_keys(WRONG_EMAIL)
        password_imput = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(PASSWORD_INPUT))
        password_imput.send_keys(PASSWORD)
        repeat_password_imput = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(REPEAT_PASSWORD_INPUT))
        repeat_password_imput.send_keys(PASSWORD)
        browser.find_element(*REGISTRATION_SUBMIT_BUTTON ).click()
        assert WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(ERROR_REGISTRATION_SPAN)).text == 'Ошибка', 'Сообщение об ошибке регистрации не появилось'

    def test_registration_page_wrong_email_shows_red_email_field_borders(self, browser, open_registration_form):
        """Тест проверяет при некорректном вводе email во время регистрации обводка становится крассной"""
        email_imput = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(EMAIL_INPUT))
        email_imput.send_keys(WRONG_EMAIL)
        password_imput = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(PASSWORD_INPUT))
        password_imput.send_keys(PASSWORD)
        repeat_password_imput = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(REPEAT_PASSWORD_INPUT))
        repeat_password_imput.send_keys(PASSWORD)
        browser.find_element(*REGISTRATION_SUBMIT_BUTTON ).click()
        error_borders = WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(EMAIL_DIV))
        assert error_borders.value_of_css_property("border-color") == 'rgb(149, 148, 171)', f'Крассная обводка для поля Email не появилась'

    def test_registration_page_wrong_email_shows_red_password_field_borders(self, browser, open_registration_form):
        """Тест проверяет при некорректном вводе email во время регистрации обводка становится крассной"""
        email_imput = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(EMAIL_INPUT))
        email_imput.send_keys(WRONG_EMAIL)
        password_imput = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(PASSWORD_INPUT))
        password_imput.send_keys(PASSWORD)
        repeat_password_imput = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(REPEAT_PASSWORD_INPUT))
        repeat_password_imput.send_keys(PASSWORD)
        browser.find_element(*REGISTRATION_SUBMIT_BUTTON ).click()
        error_borders = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(PASSWORD_DIV))
        assert error_borders.value_of_css_property("border-color") == 'rgb(149, 148, 171)', f'Крассная обводка для поля «Пароль» не появилась'

    def test_registration_page_wrong_email_shows_red_repeat_password_field_borders(self, browser, open_registration_form):
        """Тест проверяет при некорректном вводе email во время регистрации обводка становится крассной"""
        email_imput = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(EMAIL_INPUT))
        email_imput.send_keys(WRONG_EMAIL)
        password_imput = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(PASSWORD_INPUT))
        password_imput.send_keys(PASSWORD)
        repeat_password_imput = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(REPEAT_PASSWORD_INPUT))
        repeat_password_imput.send_keys(PASSWORD)
        browser.find_element(*REGISTRATION_SUBMIT_BUTTON ).click()
        error_borders = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(REPEAT_PASSWORD_DIV))
        assert error_borders.value_of_css_property("border-color") == 'rgb(149, 148, 171)', f'Крассная обводка для поля «Повторите пароль» не появилась'

    def test_registration_page_registration_an_existing_user_shows_error_message(self, browser, registration_user, open_registration_form):
        """Тест проверяет при регистрации существующего пользователя выводится сообщение об ошибке"""
        email = registration_user
        email_imput = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(EMAIL_INPUT))
        email_imput.send_keys(email)
        password_imput = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(PASSWORD_INPUT))
        password_imput.send_keys(PASSWORD)
        repeat_password_imput = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(REPEAT_PASSWORD_INPUT))
        repeat_password_imput.send_keys(PASSWORD)
        browser.find_element(*REGISTRATION_SUBMIT_BUTTON ).click()
        error_massege = WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(ERROR_REGISTRATION_SPAN))
        assert error_massege.text == 'Ошибка', 'Сообщение об ошибке регистрации не появилось'

    def test_registration_page_registration_an_existing_user_shows_red_email_field_borders(self, browser, registration_user, open_registration_form):
        """Тест проверяет при регистрации существующего пользователя обводка поеле ввода email становится крассной"""
        email = registration_user
        email_imput = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(EMAIL_INPUT))
        email_imput.send_keys(email)
        password_imput = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(PASSWORD_INPUT))
        password_imput.send_keys(PASSWORD)
        repeat_password_imput = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(REPEAT_PASSWORD_INPUT))
        repeat_password_imput.send_keys(PASSWORD)
        browser.find_element(*REGISTRATION_SUBMIT_BUTTON ).click()
        error_borders = WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(EMAIL_DIV))
        assert error_borders.value_of_css_property("border-color") == 'rgb(149, 148, 171)', f'Крассная обводка для поля Email не появилась'

    def test_registration_page_registration_an_existing_user_shows_red_password_field_borders(self, browser, registration_user, open_registration_form):
        """Тест проверяет при регистрации существующего пользователя обводка поеле ввода «Пароль» становится крассной"""
        email = registration_user
        email_imput = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(EMAIL_INPUT))
        email_imput.send_keys(email)
        password_imput = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(PASSWORD_INPUT))
        password_imput.send_keys(PASSWORD)
        repeat_password_imput = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(REPEAT_PASSWORD_INPUT))
        repeat_password_imput.send_keys(PASSWORD)
        browser.find_element(*REGISTRATION_SUBMIT_BUTTON ).click()
        error_borders = WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(PASSWORD_DIV))
        assert error_borders.value_of_css_property("border-color") == 'rgb(149, 148, 171)', f'Крассная обводка для поля «Пароль» не появилась'

    def test_registration_page_registration_an_existing_user_shows_red_repeat_password_field_borders(self, browser, registration_user, open_registration_form):
        """Тест проверяет при регистрации существующего пользователя обводка поеле ввода «Повторите пароль» становится крассной"""
        email = registration_user
        email_imput = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(EMAIL_INPUT))
        email_imput.send_keys(email)
        password_imput = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(PASSWORD_INPUT))
        password_imput.send_keys(PASSWORD)
        repeat_password_imput = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(REPEAT_PASSWORD_INPUT))
        repeat_password_imput.send_keys(PASSWORD)
        browser.find_element(*REGISTRATION_SUBMIT_BUTTON ).click()
        error_borders = WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(REPEAT_PASSWORD_DIV))
        assert error_borders.value_of_css_property("border-color") == 'rgb(149, 148, 171)', f'Крассная обводка для поля «Повторите пароль» не появилась'