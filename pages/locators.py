from selenium.webdriver.common.by import By


# локаторы основной страницы
class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


# локаторы страницы логина
class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    LOGIN_EMAIL = (By.XPATH, "//input[@id='id_login-username']")
    LOGIN_PASSWORD = (By.NAME, "//input[@id='id_login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[value='Log In']")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL = (By.XPATH, "//input[@id='id_registration-email']")
    REGISTER_PASSWORD = (By.ID, "#id_registration-password1")
    REGISTER_PASSWORD_CONFIRM = (By.ID, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[value='Register']")
