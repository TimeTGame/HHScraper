from driver import create_driver
from input_methods import ConsoleInput
from page_controls.auth import LoginPage
from page_controls.vacancy_list import VacancyListPage
from logic.auth import EmailLogin, PasswordLogin, process_order
from logic.vacancy_list import VacancyList

from time import sleep
def main() -> None:
    with create_driver() as driver:
        inputter = ConsoleInput()

        login_controls = LoginPage(driver)
        vacancy_controls = VacancyListPage(driver)

        email_method = EmailLogin(login_controls, inputter)
        password_method = PasswordLogin(login_controls, inputter)

        # process_order(email_method, password_method)

        vacancy_list = VacancyList(vacancy_controls, inputter)
        c = 0

        for link in vacancy_list.get_vacancy_links():
            print(link)

            # exiting the loop for testing purposes
            if c >= 50:
                break
            else:
                c += 1

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Shutting down')
