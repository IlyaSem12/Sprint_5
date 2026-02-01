from selenium.webdriver.common.by import By
#================= Base page =================
#ЛОГО
HEADER_LOGO = (By.CSS_SELECTOR, '.header_logo__yAp5Y')
#Кнопки входа и размещения объявления
LOGIN_AND_REGISTRATION_BUTTON = (By.XPATH, './/*[@id="root"]/div/div[1]/div/button[1]')
POST_AN_AD_BUTTON = (By.XPATH, './/*[@id="root"]/div/div[1]/div/button[2]')
#Аватар пользователя
AVATAR_BUTTON = (By.XPATH, './/*[@id="root"]/div/div[1]/div/div[1]/button')
#Имя пользователя
USERNAME_HEADER = (By.XPATH, './/*[@id="root"]/div/div[1]/div/div[1]/div/h3')
#Кноапка выхода для пользователя
EXIT_BUTTON = (By.XPATH,'//*[@id="root"]/div/div[1]/div/div[1]/div/button')
#================= Login and Registraton page =================
#Кнопка перехода на форму регистраци
NO_ACCOUNT_BUTTON= (By.XPATH, './/*[@id="root"]/div/div[2]/div[5]/form/div[3]/button[2]')
#Заголовок формы логина и регистрации
HEADER_LOGIN_AND_REGISTRATION = (By.XPATH, './/*[@id="root"]/div/div[2]/div[5]/form/div[1]/h1')
#Поля ввода для email и пароля
EMAIL_INPUT = (By.XPATH, './/*[@id="root"]/div/div[2]/div[5]/form/div[2]/div[1]/div/div/input')
PASSWORD_INPUT = (By.XPATH, './/*[@id="root"]/div/div[2]/div[5]/form/div[2]/div[2]/div/div/input')
REPEAT_PASSWORD_INPUT = (By.XPATH, './/*[@id="root"]/div/div[2]/div[5]/form/div[2]/div[3]/div/div/input')
#Контур для полей email и пароля
EMAIL_DIV = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[2]/div[1]/div/div')
PASSWORD_DIV = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[2]/div[2]/div/div')
REPEAT_PASSWORD_DIV = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[2]/div[3]/div/div')
#Кнопка подтверждения регистрации
SUBMIT_BUTTON = (By.XPATH, './/*[@id="root"]/div/div[2]/div[5]/form/div[3]/button[1]')
#Сообщение об ошибке при регистрации
ERROR_REGISTRATION_SPAN = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/form/div[2]/div[1]/span')

#================= Creating Ad page =================
#Поле ввода названия товара
NAME_PRODUCT_INPUT = (By.XPATH, '//*[@id="root"]/div/div[2]/div/form/div[2]/div[1]/div/div/input')
#кнопка для расскрытия DROPDOWN MENU категории товара
CATEGORY_DROPDOWN_MENU_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[2]/div/form/div[2]/div[2]/div[1]/button')
#кнопка выбора категории "Технологии"
CATEGORY_TECHNOLOGY_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[2]/div/form/div[2]/div[2]/div[1]/button')
#кнопка для расскрытия DROPDOWN MENU города
CITY_DROPDOWN_MENU_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[2]/div/form/div[3]/div[1]/button')
#кнопка выбора гророда Санкт-питербург 
CITY_SAINT_PETERSBURG_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[2]/div/form/div[3]/div[2]/button[2]')
#RadioButton Б/У
USED_CONDITION_RADIOBUTTON = (By.XPATH, '//*[@id="root"]/div/div[2]/div/form/fieldset/div/div[2]/div')
#Поле ввода описания товара
DISCRIPTION_ITEM_TEXTAREA = (By.XPATH, '//*[@id="root"]/div/div[2]/div/form/div[4]/div/textarea')
#Поле ввода Цены товара
PRICE_INPUT = (By.XPATH, '//*[@id="root"]/div/div[2]/div/form/div[5]/div/div/input')

PUBLISH_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[2]/div/form/button')
#================= Creating Ad page =================
MY_ADS_CARD = (By.XPATH, '//*[@id="root"]/div/div[2]/div[4]/div/div[1]/div')
MY_ADS_TITLES = (By.XPATH, '//*[@id="root"]/div/div[2]/div[4]/div/div[1]/div/div/div[1]/h2')
