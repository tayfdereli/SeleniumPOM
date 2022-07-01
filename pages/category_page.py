from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CategoryPage(BasePage):
    BREADCRUMB = (By.CLASS_NAME, 'breadcrumb')
    BREADCRUMB_LAST = (By.CSS_SELECTOR, 'li[itemprop]:last-child')
    PRODUCTS = (By.CLASS_NAME, 'product-item')

    def get_breadcrumb_text(self):
        return self.find_element(*self.BREADCRUMB).text

    def get_breadcrumb_last_text(self):
        return self.find_element(*self.BREADCRUMB_LAST).text

    def click_product(self, index):
        self.find_elements(index, *self.PRODUCTS)
