from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.SUBMIT_BT = (By.CSS_SELECTOR, "button[type='submit']")
        self.EMAIL_CHOOSE_BT = (By.CSS_SELECTOR, "input[type='radio'][value='email'] + span")
        self.EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='login'][inputmode='email']")
        self.PASSWORD_OPTION_BT = (By.CSS_SELECTOR, "button[data-qa='expand-login-by-password']")
        self.PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password'][type='password'][data-qa='applicant-login-input-password']")

    def goto_login_page(self):
        self.driver.get('https://hh.ru/account/login')
        self.driver.implicitly_wait(10)

    def submit_button_click(self):
        self.driver.find_element(*self.SUBMIT_BT).click()

    def choose_email_option(self):
        self.driver.find_element(*self.EMAIL_CHOOSE_BT).click()

    def enter_email(self, email: str):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def choose_password_auth(self):
        self.driver.find_element(*self.PASSWORD_OPTION_BT).click()

    def enter_password(self, password: str):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
