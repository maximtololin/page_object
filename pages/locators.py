from selenium.webdriver.common.by import By


# локаторы основной страницы
class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


# локаторы страницы логина
class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    LOGIN_EMAIL = (By.XPATH, "//input[@id='id_login-username']")
    LOGIN_PASSWORD = (By.NAME, "//input[@id='id_login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[value='Log In']")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL = (By.XPATH, "//input[@id='id_registration-email']")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[value='Register']")


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, "h1:nth-child(1)")
    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages > div:nth-of-type(1) strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div[class='col-sm-6 product_main'] p[class='price_color']")
    BASKET_TOTAL_PRICE = (By.CSS_SELECTOR, "div[class='alertinner '] p strong")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button[value='Add to basket']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")


class BasketPageLocators:
    BASKET_PAGE = (By.CSS_SELECTOR, "a[class='btn btn-default']")
    # подтверждаем наличие товара с помощью наличия кнопки "удалить"
    PRODUCTS_IN_BASKET = (By.XPATH, "//a[normalize-space()='Remove']")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "p:nth-child(1)")
