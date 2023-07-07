from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Locators(BasePage):
    # Локаторы

    # Заголовок страницы в правой части
    LOCATOR_PAGE_RIGHT = (By.XPATH, '//*[@id="page-right"]/div/div/h1')

    # Кнопка 'Телефон'
    LOCATOR_BTN_PHONE = (By.ID, "t-btn-tab-phone")

    # Кнопка 'Почта'
    LOCATOR_BTN_MAIL = (By.ID, "t-btn-tab-mail")

    # Кнопка 'Войти'
    LOCATOR_BTN_LOGIN = (By.ID, "t-btn-tab-login")

    # Кнопка 'ЛС'
    LOCATOR_BTN_LS = (By.ID, "t-btn-tab-ls")

    # Поле ввода для почты
    LOCATOR_INPUT_MAIL = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')

    # Поле ввода для имени пользователя
    LOCATOR_INPUT_USERNAME = (By.ID, 'username')

    # Поле ввода для пароля
    LOCATOR_INPUT_PASSWORD = (By.ID, 'password')

    # Кнопка 'Войти'
    LOCATOR_BTN_ENTER = (By.ID, 'kc-login')

    # Кнопка 'Выйти'
    LOCATOR_BTN_LOGOUT = (By.ID, 'logout-btn')

    # Сообщение об ошибке
    LOCATOR_ERROR_MSG = (By.XPATH, "//span[@id='form-error-message']")

    # Сообщение об отсутствующем имени пользователя
    LOCATOR_EMPTY_USERNAME_MSG = (By.CSS_SELECTOR, '.rt-input-container__meta--error')

    # Кнопка 'Забыли пароль?'
    LOCATOR_FORGOT_PASSWORD = (By.ID, 'forgot_password')

    # Кнопка 'Зарегистрироваться'
    LOCATOR_REGISTER = (By.XPATH, "//a[@id='kc-register']")

    # Активная вкладка
    LOCATOR_ACTIVE_TAB = (By.CSS_SELECTOR, '.rt-tab.rt-tab--small.rt-tab--active')

    # Кнопка 'Вконтакте'
    LOCATOR_SOCIAL_NETWORK_VK = (By.ID, "oidc_vk")

    # Идентификатор 'Вход в VK ID'
    LOCATOR_IDENTIFIER_VK = (By.XPATH, "// div[contains(text(), 'Вход в VK ID')]")

    # Кнопка 'Одноклассники'
    LOCATOR_SOCIAL_NETWORK_OK = (By.ID, "oidc_ok")

    # Идентификатор 'Одноклассники'
    LOCATOR_IDENTIFIER_OK = (By.XPATH, "//div[contains(text(),'Одноклассники')]")

    # Кнопка 'Мой Мир@Mail.Ru'
    LOCATOR_SOCIAL_MAIL = (By.ID, "oidc_mail")

    # Идентификатор 'Мой Мир@Mail.Ru'
    LOCATOR_IDENTIFIER_MAIL = (By.XPATH, "// span[contains(text(), 'Мой Мир@Mail.Ru')]")

    # Кнопка 'Яндекс'
    LOCATOR_SOCIAL_YANDEX = (By.ID, "oidc_ya")

    # Идентификатор 'Яндекс'
    LOCATOR_IDENTIFIER_YANDEX = (By.XPATH, "//*[@id='UserEntryFlow']/form/div/div[1]/h1")

    # Активная вкладка 'Пользовательское соглашение'
    LOCATOR_AGREEMENT = (By.XPATH, "//a[@class='rt-link rt-link--orange' and @href='https://b2c.passport.rt.ru/sso-static/agreement/agreement.html']")

    # Идентификатор текста соглашения
    LOCATOR_AGREEMENT_ROOT = (By.ID, "root")


    # Тексты сообщений

    # Сообщение об ошибке при неверных данных
    ERROR_MSG_INVALID_DATA = 'Неверный логин или пароль'

    # Сообщение об ошибке при неверной капче
    ERROR_MSG_INVALID_CAPTCHA = 'Неверно введен текст с картинки'

    # Сообщение об отсутствующем номере телефона
    EMPTY_PHONE_MSG = 'Введите номер телефона'

    # Сообщение об отсутствующей почте
    EMPTY_MAIL_MSG = 'Введите адрес, указанный при регистрации'

    # Сообщение об отсутствующем имени пользователя
    EMPTY_LOGIN_MSG = 'Введите логин, указанный при регистрации'

    # Сообщение об отсутствующем ЛС
    EMPTY_LS_MSG = 'Введите номер вашего лицевого счета'

    # Заголовок страницы авторизации
    TITLE_AUTH = 'Авторизация'

    # Заголовок страницы восстановления пароля
    TITLE_RECOVERY = 'Восстановление пароля'

    # Заголовок страницы регистрации
    TITLE_REGISTRATION = 'Регистрация'
