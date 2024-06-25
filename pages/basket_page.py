from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage (BasePage):
    def basket_has_no_items (self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM)
    
    def basket_has_label_empty (self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_LABEL)