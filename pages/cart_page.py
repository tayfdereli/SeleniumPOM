from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    CART_HEADER = (By.TAG_NAME, 'h1')
    ITEM_REMOVE_BTN = (By.CLASS_NAME, 'remove-from-cart')
    CART_ALERT = (By.CLASS_NAME, 'no-items')

    def __init__(self, driver):
        super().__init__(driver)
        self.check()

    def check(self):
        self.wait_element(self.CART_HEADER, 'No Cart Header on the page !')
        self.wait_element(self.ITEM_REMOVE_BTN, 'No Cart Header on the page !')

    def get_cart_header_text(self):
        return self.find_element(*self.CART_HEADER).text

    def click_remove_product(self):
        self.click_element(*self.ITEM_REMOVE_BTN)

    def get_cart_alert_text(self):
        return self.find_element(*self.CART_ALERT).text
