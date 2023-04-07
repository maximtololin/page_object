from pages.base_page import BasePage
from pages.locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import math
import time


class ProductPage(BasePage):

    def product_should_in_basket(self):
        self.add_product_to_basket()
        self.solve_quiz_and_get_code()
        time.sleep(2)
        self.get_product_name()
        self.get_product_price()
        self.check_success_message()
        self.check_basket_total()
        self.compare_values_of_product_names()
        self.compare_values_of_product_prices()

    # метод для добавления товара в корзину
    def add_product_to_basket(self):
        self.find_element(ProductPageLocators.ADD_TO_BASKET_BUTTON).click(), "Product out of basket"

    # метод для получения названия товара
    def get_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Out of product name"

    # метод для получения цены товара
    def get_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Out of product price"

    # метод для проверки сообщения об успешном добавлении товара в корзину
    def check_success_message(self):

        assert self.is_element_present(*ProductPageLocators.BASKET_PRODUCT_NAME), "Wrong product in success message "

    # метод для сравнения названия продукта
    def compare_values_of_product_names(self):
        value_one = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        value_two = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_NAME).text
        assert value_one == value_two, "Name of product - incorrect!"

    # метод для сравнения цены продукта
    def compare_values_of_product_prices(self):
        value_one = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        value_two = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE).text
        assert value_one == value_two, "Price of product - incorrect!"

    # метод для проверки общей стоимости корзины
    def check_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL_PRICE), "Wrong basket total"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        time.sleep(2)
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
