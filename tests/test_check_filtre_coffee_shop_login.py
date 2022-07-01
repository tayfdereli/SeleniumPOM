import unittest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from pages.category_page import CategoryPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from tests.base_test import BaseTest


class TestCheckFiltreCoffeShop(BaseTest):
    invalid_email = 'Selenium@testmail.com'
    password = 'SeleniumSessionTest123'
    login_alert_text_messsage = 'Kimlik doğrulama başarısız.'
    valid_email = 'wabomej221@3dinews.com'
    user_name = 'Selenium Session'
    category_name = 'Kahvelerimiz'
    category_text = 'KAHVELERIMIZ'
    cart_popup_alert_text = 'Ürün başarı ile sepete eklenmiştir'
    cart_header_text = 'ALIŞVERIŞ SEPETI'
    cart_alert_text = 'Sepetinizde ürün bulunmamaktadır.'
    item_index = 0

    def test_check_filtre_coffee_shop_login(self):
        home_page = HomePage(self.driver)
        home_page.click_hesabim()
        login_page = home_page.click_giris_yap()

        login_page.fill_email_text_box(self.invalid_email)
        login_page.fill_password_text_box(self.password)
        login_page.click_signin_btn()
        self.assertEqual(self.login_alert_text_messsage, login_page.get_alert_message())

        login_page.fill_email_text_box(self.valid_email)
        login_page.fill_password_text_box(self.password)
        login_page.click_signin_btn()
        home_page.click_hesabim()
        self.assertEqual(self.user_name, home_page.get_user_name())

        home_page.click_category(self.category_name)
        category_page = CategoryPage(self.driver)
        self.assertIn(self.category_text, category_page.get_breadcrumb_text())
        self.assertEqual(self.category_text, category_page.get_breadcrumb_last_text())
        category_page.click_product(self.item_index)

        product_page = ProductPage(self.driver)
        self.assertTrue(product_page.is_present_add_to_cart_btn())
        product_page.click_add_to_cart_btn()
        self.assertIn(self.cart_popup_alert_text, product_page.get_cart_popup_alert_text())

        cart_page = product_page.click_odeme_adimina_gec_btn()
        self.assertEqual(self.cart_header_text, cart_page.get_cart_header_text())
        cart_page.click_remove_product()
        self.assertEqual(self.cart_alert_text, cart_page.get_cart_alert_text(), 'Mesajın eşleşmedi')

    def tearDown(self):
        self.driver.quit()
