from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import BasePageLocators, BasketPageLocators


# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
# link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"

# self — это ссылка на текущий экземпляр класса с которым вы работаете в данный момент

# В конструктор BasePage добавим команду для неявного ожидания со значением по умолчанию в 10

# В этом же классе реализуем метод is_element_present, в котором будем перехватывать исключение.
# В него будем передавать два аргумента: как искать (css, id, xpath и тд) и собственно что искать (строку-селектор).
class BasePage:
    # метод вызывается, когда мы создаем объект
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_login_page(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def go_to_basket_page(self):
        self.browser.find_element(*BasketPageLocators.BASKET_PAGE).click()

    # метод для нахождения элемента
    def find_element(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator),
                                                       message=f"Can't find element by locator {locator}")

    # добавим метод, открывающий нужную страницу в браузере
    def open(self):
        self.browser.get(self.url)

    # добавим метод, проверяющий наличие элемента на странице или его отсутствие
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    # добавим метод, который проверяет отсутствие элемента на странице
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    # добавим метод, который проверяет исчезновение элемента на странице
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True
