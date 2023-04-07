from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages import locators


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

