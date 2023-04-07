from pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('promo_offer', [
    "0", "1", "3", "4", "5", "6",
    pytest.param("7", marks=pytest.mark.xfail(reason="Nice Bug")),
    "8", "9", "10"
])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.product_should_in_basket()

# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
# link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
