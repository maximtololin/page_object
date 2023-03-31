from selenium.common.exceptions import NoSuchElementException


# self — это ссылка на текущий экземпляр класса с которым вы работаете в данный момент

# В конструктор BasePage добавим команду для неявного ожидания со значением по умолчанию в 10

# В этом же классе реализуем метод is_element_present, в котором будем перехватывать исключение.
# В него будем передавать два аргумента: как искать (css, id, xpath и тд) и собственно что искать (строку-селектор).
class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, selector, value):
        try:
            self.browser.find_element(selector, value)
        except NoSuchElementException:
            return False
        return True
