from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket (browser):
    # Navigating to link
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    # Click Add to cart
    page.add_to_cart()
    # In alert modal enter calculation result
    page.solve_quiz_and_get_code()
    # Assert product name: it should be the same in toast message
    page.check_product_name()
    # Assert price: price should be displayed in toast message
    page.check_product_price()
    time.sleep(10)