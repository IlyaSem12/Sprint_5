from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
from config import *


class TestLogoutUser:
    def test_main_page_success_logout_user_is_displayed_login_and_registration_buttton(self,browser,login_user):
        """Тест проверяет, что после выхода из аккауната пользоваетля вместо автара и имени отображается кнопка «Вход и регистрация»."""
        webdrivwer =  WebDriverWait(browser, 5)
        webdrivwer.until(expected_conditions.element_to_be_clickable(EXIT_BUTTON)).click()
        assert webdrivwer.until(expected_conditions.visibility_of_element_located(LOGIN_AND_REGISTRATION_BUTTON)).is_displayed() == True, 'Отсутвует кнопка «Вход и регистрация»'

    def test_main_page_success_logout_user_is_not_displayed_user_avatar(self, browser, login_user):
        """Тест проверяет, что после выхода из аккауната пользоваетля отсутвует аватр пользователя"""
        webdrivwer =  WebDriverWait(browser, 5)
        webdrivwer.until(expected_conditions.element_to_be_clickable(EXIT_BUTTON)).click()
        assert webdrivwer.until(expected_conditions.invisibility_of_element(AVATAR_BUTTON)) == True , "Аватар пользователя должен отсутствовать" 
    
    def test_main_page_logout_user_is_not_displayed_user_name(self,browser,login_user):
        """Тест проверяет, что после выхода из аккауната пользоваетля отсутвует имя пользователя"""
        webdrivwer =  WebDriverWait(browser, 5)
        webdrivwer .until(expected_conditions.element_to_be_clickable(EXIT_BUTTON)).click()
        assert WebDriverWait(browser, 3).until(expected_conditions.invisibility_of_element(USERNAME_HEADER)) == True, "Имя пользователя должено отсутствовать"