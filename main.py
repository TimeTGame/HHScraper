from driver import driver
from input_methods import ConsoleInput, InputMethod
from page_controls.auth import LoginPage
from logic.auth import EmailLogin, PasswordLogin, process_order

def main() -> None:
    inputter = ConsoleInput()
    controls = LoginPage(driver)

    email_method = EmailLogin(controls, inputter)
    password_method = PasswordLogin(controls, inputter)

    process_order(email_method, password_method)

if __name__ == "__main__":
    try:
        main()
    finally:
        driver.quit()