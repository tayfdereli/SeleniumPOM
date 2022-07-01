from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.cart_page import CartPage


class ProductPage(BasePage):
    ADD_TO_CART_BTN = (By.CLASS_NAME, 'add-to-cart')
    CART_POPUP_ALERT_TEXT = (By.ID, 'myModalLabel')
    ODEME_ADIMINA_GEC_BTN = (By.CSS_SELECTOR, '.cart-content-btn .btn-primary')

    def is_present_add_to_cart_btn(self):
        return self.find_element(*self.ADD_TO_CART_BTN)

    def click_add_to_cart_btn(self):
        self.click_element(*self.ADD_TO_CART_BTN)

    def get_cart_popup_alert_text(self):
        return self.wait_element(self.CART_POPUP_ALERT_TEXT).text

    def click_odeme_adimina_gec_btn(self):
        self.click_element(*self.ODEME_ADIMINA_GEC_BTN)

        return CartPage(self.driver)
