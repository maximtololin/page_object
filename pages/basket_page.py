from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):


    # создаем метод для проверки, что в корзине нет товаров
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), \
            "Products in basket are presented, but should not be"

    # создаем метод для проверки, что есть текст о том, что корзина пуста
    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "Empty basket message is not presented, but should be"
