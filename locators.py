from selenium.webdriver.common.by import By
#================= Base page =================
#ЛОГО
HEADER_LOGO = (By.CSS_SELECTOR, "svg[class^='header_logo']")
#Кнопки входа и размещения объявления
LOGIN_AND_REGISTRATION_BUTTON = (By.XPATH, "//button[normalize-space()='Вход и регистрация']")
POST_AN_AD_BUTTON = (By.XPATH, "//button[normalize-space()='Разместить объявление']")
#Аватар пользователя
AVATAR_BUTTON = (By.CSS_SELECTOR, "button.circleSmall")
#Имя пользователя
USERNAME_HEADER = (By.CSS_SELECTOR, "h3.profileText.name")
#Кноапка выхода для пользователя
EXIT_BUTTON = (By.XPATH,"//button[normalize-space()='Выйти']")
#================= Login and Registraton page =================
#Кнопка перехода на форму регистраци
NO_ACCOUNT_BUTTON= (By.XPATH, "//button[normalize-space()='Нет аккаунта']")
#Заголовок формы логина и регистрации
HEADER_CREATE_AD_AUTH_REQUIRED = (By.XPATH, "//h1[normalize-space()='Чтобы разместить объявление, авторизуйтесь']")
HEADER_REGISTRATION = (By.XPATH, "//h1[normalize-space()='Зарегистрироваться']")
HEADER_LOGIN = (By.XPATH, "//h1[normalize-space()='Войти']")
#Поля ввода для email и пароля
EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")
PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
REPEAT_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='submitPassword']")
#Контур для полей email и пароля
EMAIL_DIV = (By.XPATH, "//input[@name='email']/parent::div")
PASSWORD_DIV = (By.XPATH, "//input[@name='password']/parent::div")
REPEAT_PASSWORD_DIV = (By.XPATH, "//input[@name='submitPassword']/parent::div")
#Кнопка подтверждения регистрации
REGISTRATION_SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit' and normalize-space()='Создать аккаунт']")
LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit' and normalize-space()='Войти']")
#Сообщение об ошибке при регистрации
ERROR_REGISTRATION_SPAN = (By.XPATH, "//span[normalize-space()='Ошибка']")
#================= Creating Ad page =================
#Поле ввода названия товара
NAME_PRODUCT_INPUT = (By.XPATH, "//input[@name='name']")
#кнопка для расскрытия DROPDOWN MENU категории товара
CATEGORY_DROPDOWN_MENU_BUTTON = (By.XPATH, "//input[@name='category']/following-sibling::button[1]")
#кнопка выбора категории "Технологии"
CATEGORY_TECHNOLOGY_BUTTON = (By.XPATH, "//button[.//span[normalize-space()='Технологии']]")
#кнопка для расскрытия DROPDOWN MENU города
CITY_DROPDOWN_MENU_BUTTON = (By.XPATH, "//input[@name='city']/following-sibling::button[1]")
#кнопка выбора гророда Санкт-питербург 
CITY_SAINT_PETERSBURG_BUTTON = (By.XPATH, "//button[.//span[normalize-space()='Санкт-Петербург']]")
#RadioButton Б/У
USED_CONDITION_RADIOBUTTON = (By.XPATH, "//label[normalize-space()='Б/У']/preceding-sibling::div[1]")
#Поле ввода описания товара
DISCRIPTION_ITEM_TEXTAREA = (By.XPATH, "//textarea[@name='description']")
#Поле ввода Цены товара
PRICE_INPUT = (By.XPATH, "//input[@name='price']")
#Кнопка публикации
PUBLISH_BUTTON = (By.XPATH, "//button[@type='submit' and normalize-space()='Опубликовать']")
#================= Creating Ad page =================
MY_ADS_CARD = (By.XPATH, "//div[contains(@class,'card')]")
MY_ADS_TITLES = (By.XPATH, "//div[contains(@class,'card')]//h2")
