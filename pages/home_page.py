from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.login_page import LoginPage


class HomePage(BasePage):
    HESABIM = (By.ID, '_desktop_user_info')
    GIRIS_YAP = (By.XPATH, '//ul//span[text()="Giris Yap"]')
    USER_NAME_TEXT = (By.CSS_SELECTOR, '#header-menu-content .account span')
    CATEGORY_NAME = '//a[contains(text(),"{}")]'

    def click_hesabim(self):
        self.click_element(*self.HESABIM)

    def click_giris_yap(self):
        self.click_element(*self.GIRIS_YAP)

        return LoginPage(self.driver)

    def get_user_name(self):
        return self.wait_element(self.USER_NAME_TEXT).text

    def click_category(self, category):
        self.click_element(By.XPATH, self.CATEGORY_NAME.format(category))
