import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import os
import sys
from time import sleep
from abc import ABC, abstractmethod

parent_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')
)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from config import LOGIN_PAGE_URL
from config import ch_input_method as input_method
from driver import driver


input_getter = input_method().get_input

def goto_login_page() -> None:
    driver.get(LOGIN_PAGE_URL)
    driver.implicitly_wait(10)

class LoginMethod(ABC):
    @abstractmethod
    def login():
        pass


class EmailLogin(LoginMethod):
    def login(self) -> bool:
        goto_login_page()

        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()

        email_choose_button = driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='email'] + span")
        email_choose_button.click()
        email_input = driver.find_element(By.CSS_SELECTOR, "input[name='login'][inputmode='email']")

        email = input_getter('email')

        email_input.send_keys(email)

        return True


class PasswordLogin(LoginMethod):
    def login(self) -> bool:
        login_password_bt = driver.find_element(By.CSS_SELECTOR, "button[data-qa='expand-login-by-password']")
        login_password_bt.click()

        password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password'][type='password'][data-qa='applicant-login-input-password']")

        password = input_getter('password')

        password_input.send_keys(password)
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()

        return True


def process_order(phase1process: LoginMethod, phase2process: LoginMethod):
    if phase1process.login():
        print('Phase 1 loggigning Success!')

    if phase2process.login():
        print('Phase 2 loggigning Success!')

email_method = EmailLogin()
password_method = PasswordLogin()

# process_order(email_method, password_method)

# all_cookies = {cookie['name']: cookie['value'] for cookie in driver.get_cookies()}
# print(all_cookies)
