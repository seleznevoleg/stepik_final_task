from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators ():
    LOGIN_USER_FIELD = (By.ID, "id_login-username")
    LOGIN_PASSWORD_FIELD = (By.ID, "id_login-password")
    REGISTER_EMAIL_FIELD = (By.ID, "id_registration-email")
    REGISTER_PASSWORD_FIELD = (By.ID, "id_registration-password1")
    REGISTER_PASSWORD_CONFIRMATION_FIELD = (By.ID, "id_registration-password2")
    REGISTER_SUBMIT = (By.CSS_SELECTOR, "[name=\"registration_submit\"]")

class ProductPageLocators ():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "[value=\"Add to basket\"]")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6 > .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6 > h1")
    PRODUCT_NAME_IN_TOAST = (By.CSS_SELECTOR, ".alert-success > .alertinner > strong") # Here could be an issues
    PRODUCT_PRICE_IN_TOAST = (By.CSS_SELECTOR, ".alert-info > .alertinner > p > strong")
    ADD_SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")

class BasePageLocators ():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini >  .btn-group > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators ():
    EMPTY_BASKET_LABEL = (By.CSS_SELECTOR, "[id=\"content_inner\"] > p")
    BASKET_ITEM = (By.CLASS_NAME, "basket-items")