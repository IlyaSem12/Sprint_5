from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
from config import *
from helpers import *


class TestCreatingAd:

    def test_main_page_сreating_ad_unauthorized_user_shows_auth_modal_for_unauthorized_user(self,browser):
        """Тест проверяет, что при попытке разместить объявление неавторизованный пользователь
            видит модальное окно с заголовком «Чтобы разместить объявление, авторизуйтесь»."""
        webdrivwer =  WebDriverWait(browser, 5)
        browser.find_element(*POST_AN_AD_BUTTON).click()
        assert webdrivwer.until(expected_conditions.visibility_of_element_located(HEADER_CREATE_AD_AUTH_REQUIRED)), 'Модальное окно с заголовком «Чтобы разместить объявление, авторизуйтесь» не появилось'

    def test_crating_ad_page_success_сreating_ad_authorized_user_shows_ad_in_profile(self,browser, open_create_listing_page):
        """Тест проверяет, что пользователь создаёт объявление и видит его в профиле в блоке 'Мои объявления'."""
        webdrivwer = WebDriverWait(browser, 10)
        product_name = generate_product_name()
        name_input = webdrivwer.until(expected_conditions.visibility_of_element_located(NAME_PRODUCT_INPUT))
        name_input.clear()
        name_input.send_keys(product_name)
        webdrivwer.until(expected_conditions.element_to_be_clickable(CATEGORY_DROPDOWN_MENU_BUTTON)).click()
        webdrivwer.until(expected_conditions.element_to_be_clickable(CATEGORY_TECHNOLOGY_BUTTON)).click()
        webdrivwer.until(expected_conditions.element_to_be_clickable(CITY_DROPDOWN_MENU_BUTTON)).click()
        webdrivwer.until(expected_conditions.element_to_be_clickable(CITY_SAINT_PETERSBURG_BUTTON)).click()
        webdrivwer.until(expected_conditions.element_to_be_clickable(USED_CONDITION_RADIOBUTTON)).click()
        desc = webdrivwer.until(expected_conditions.visibility_of_element_located(DISCRIPTION_ITEM_TEXTAREA))
        desc.send_keys(DESCRIPTION_PRODUCT)
        price = webdrivwer.until(expected_conditions.visibility_of_element_located(PRICE_INPUT))
        price.send_keys(str(PRICE_PRODUCT))
        webdrivwer.until(expected_conditions.element_to_be_clickable(PUBLISH_BUTTON)).click()
        webdrivwer.until(expected_conditions.url_to_be(BASE_URL))
        webdrivwer.until(expected_conditions.element_to_be_clickable(AVATAR_BUTTON)).click()
        webdrivwer.until(expected_conditions.visibility_of_element_located(MY_ADS_CARD))
        titles = browser.find_element(*MY_ADS_TITLES).text
        assert product_name in titles, f"Созданное объявление не найдено в 'Мои объявления'"