import pytest
import requests
from locators import *
from config import *
from selenium import webdriver 
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions
from helpers import *

@pytest.fixture
def browser():
    '''Фикструа для получения инстанса драйвера'''
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(autouse=True)
def open_base_page(browser):
    """Фикстура для перехода на главную страницу"""
    browser.get(BASE_URL) #переходим по ссылке
    #добавляем явное ожиданяие для прогрузки страницы
    WebDriverWait(browser, 5).until(expected_conditions.presence_of_element_located(HEADER_LOGO)) 
    
@pytest.fixture
def open_registration_form(browser):
    """Фикстура для открытия формы регистрации"""
    WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable(LOGIN_AND_REGISTRATION_BUTTON)).click() 
    WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable(NO_ACCOUNT_BUTTON)).click()
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(HEADER_LOGIN_AND_REGISTRATION))
    
@pytest.fixture
def open_login_form(browser):
    """Фикстура для открытия формы Входа"""
    WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable(LOGIN_AND_REGISTRATION_BUTTON)).click() 
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(HEADER_LOGIN_AND_REGISTRATION))

@pytest.fixture
def open_create_listing_page(browser, login_user):
    """Фикстура для открытия формы Входа"""
    browser.get(CREATING_LISTING_URL)#переходим по ссылке

@pytest.fixture
def registration_user():
    """Фикстура для создания пользователя"""
    email = generate_email()
    payload = {'email': email, 'password': PASSWORD , 'submitPassword': PASSWORD}
    requests.post(SIGNUP_URL, json=payload,  headers = {"Content-Type": "application/json"})
    return email

@pytest.fixture
def login_user(browser,registration_user):
    """Фикстура для авторизации пользователя"""
    email = registration_user
    payload = {'email': email, 'password': PASSWORD}
    response = requests.post(SIGNIN_URL, json=payload,  headers = {"Content-Type": "application/json"})
    token = response.json()["token"]['access_token']
    user = response.json()["user"]
    browser.execute_script(
        """
        window.localStorage.setItem('token', arguments[0]);
        window.localStorage.setItem('islogin', 'true');
        window.localStorage.setItem('user', JSON.stringify(arguments[1]));
        """,
        token,
        user
    )
    browser.refresh()