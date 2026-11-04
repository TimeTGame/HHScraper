from abc import ABC, abstractmethod
from page_controls.auth import LoginPage
from input_methods import InputMethod


class LoginMethod(ABC):
    def __init__(self, controls: LoginPage, inputter: InputMethod):
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
        email = self.inputter.get_input('email')
        self.ctrl.enter_email(email)

        return True


class PasswordLogin(LoginMethod):
    def login(self) -> bool:
        self.ctrl.choose_password_auth()

        password = self.inputter.get_input('password')
        self.ctrl.enter_password(password)

        self.ctrl.submit_button_click()

        return True


def process_order(phase1process: LoginMethod, phase2process: LoginMethod):
    if phase1process.login():
        print('Phase 1 authorization Success!')

    if phase2process.login():
        print('Phase 2 authorization Success!')
