from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_TEXT_BOX = (By.NAME, 'email')
    PASSWORD_TEXT_BOX = (By.NAME, 'password')
    GIRIS_YAP_BTN = (By.ID, 'submit-login')
    ALERT = (By.CLASS_NAME, 'alert-danger')

    def fill_email_text_box(self,email):
        self.clear_text(*self.EMAIL_TEXT_BOX).send_text(email, *self.EMAIL_TEXT_BOX)

    def fill_password_text_box(self, password):
        self.send_text(password, *self.PASSWORD_TEXT_BOX)

    def click_signin_btn(self):
        self.click_element(*self.GIRIS_YAP_BTN)

    def get_alert_message(self):
        return self.wait_element(self.ALERT).text
