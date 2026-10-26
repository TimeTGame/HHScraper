from selenium import webdriver
import os
import sys
from abc import ABC, abstractmethod

parent_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')
)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from config import ch_input_method as input_method
from driver import driver
from page_controls.auth import LoginPage


controls = LoginPage(driver)
input_getter = input_method().get_input

class LoginMethod(ABC):
    def __init__(self, controls: LoginPage, inputter: input_method):
        self.ctrl = controls
        self.inputter = inputter

    @abstractmethod
    def login(self) -> bool:
        pass


class EmailLogin(LoginMethod):
    def login(self) -> bool:
        self.ctrl.goto_login_page()

        self.ctrl.submit_button_click()

        self.ctrl.choose_email_option()
        email = input_getter('email')
        self.ctrl.enter_email(email)

        return True


class PasswordLogin(LoginMethod):
    def login(self) -> bool:
        self.ctrl.choose_email_option()

        password = input_getter('password')
        self.ctrl.enter_password(password)

        self.ctrl.submit_button_click()

        return True


def process_order(phase1process: LoginMethod, phase2process: LoginMethod):
    if phase1process.login():
        print('Phase 1 loggigning Success!')

    if phase2process.login():
        print('Phase 2 loggigning Success!')

email_method = EmailLogin()
password_method = PasswordLogin()

process_order(email_method, password_method)

# all_cookies = {cookie['name']: cookie['value'] for cookie in driver.get_cookies()}
# print(all_cookies)
