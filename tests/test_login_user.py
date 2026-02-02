from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
from config import *


class TestLoginUser:

    def test_login_page_success_login_user_redirect_main_page(self,browser,registration_user, open_login_form):
        """Тест проверяет, что зарегистрированный пользователь может успешно авторизоваться и после входа происходит перенаправление на главную страницу."""
        email = registration_user
        email_imput = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(EMAIL_INPUT))
        email_imput.send_keys(email)
        password_imput = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(PASSWORD_INPUT))
        password_imput.send_keys(PASSWORD)
        browser.find_element(*SUBMIT_BUTTON ).click()
        assert BASE_URL in browser.current_url, 'Редирект на главную страницу не был произведен'

    def test_login_page_success_login_user_is_displayed_user_avatar(self, browser,registration_user, open_login_form):
        """Тест проверяет, что зарегистрированный пользователь может успешно авторизоваться и после входа в правом верхнем углу около кнопки «Разместить объявление» отображается аватар пользователя"""
        email = registration_user
        email_imput = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(EMAIL_INPUT))
        email_imput.send_keys(email)
        password_imput = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(PASSWORD_INPUT))
        password_imput.send_keys(PASSWORD)
        browser.find_element(*SUBMIT_BUTTON).click()
        assert WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(AVATAR_BUTTON)).is_displayed() == True, 'Отсутствует аватар пользователя'
    
    def test_login_page_login_user_is_displayed_user_name(self,browser,registration_user, open_login_form):
        """Тест проверяет, что зарегистрированный пользователь может успешно авторизоваться и после входа в правом верхнем углу около кнопки «Разместить объявление» отображается имя пользователя 'User.'"""
        email = registration_user
        email_imput = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(EMAIL_INPUT))
        email_imput.send_keys(email)
        password_imput = WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(PASSWORD_INPUT))
        password_imput.send_keys(PASSWORD)
        browser.find_element(*SUBMIT_BUTTON ).click()
        username = WebDriverWait(browser, 3).until(expected_conditions.visibility_of_element_located(USERNAME_HEADER))
        assert username.text == 'User.', 'Отсутствует имя пользователя'