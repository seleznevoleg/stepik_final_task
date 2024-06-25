from .pages.product_page import ProductPage

def test_guest_cant_see_success_message_after_adding_product_to_basket (browser):
    # Navigating to link
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    # Click Add to cart
    page.add_to_cart()
    page.success_message_is_not_displayed()

def test_guest_cant_see_success_message (browser):
    # Navigating to link
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    # Click Add to cart
    page.success_message_is_not_displayed()

def test_message_disappeared_after_adding_product_to_basket (browser):
    # Navigating to link
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    # Click Add to cart
    page.add_to_cart()
    page.success_message_is_desapeared()
