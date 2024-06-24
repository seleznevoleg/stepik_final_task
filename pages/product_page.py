from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_cart (self):
        add_to_cart = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        add_to_cart.click()
    def check_product_name (self):
        pruduct_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        text_product_name = pruduct_name.text
        product_name_in_toast = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_TOAST)
        text_product_name_in_toast = product_name_in_toast.text
        assert text_product_name == text_product_name_in_toast, f"Expected the texts to be equal, but got '{text_product_name}' and '{text_product_name_in_toast}'"
    def check_product_price (self):
        pruduct_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        text_product_price = pruduct_price.text
        product_price_in_toast = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_TOAST)
        text_product_price_in_toast = product_price_in_toast.text
        assert text_product_price == text_product_price_in_toast, f"Expected the texts to be equal, but got '{text_product_price}' and '{text_product_price_in_toast}'"