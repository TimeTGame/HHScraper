from driver import create_driver
from input_methods import ConsoleInput
from page_controls.auth import LoginPage
from page_controls.vacancy_list import VacancyListPage
from page_controls.vacancy import VacancyPage
from logic.auth import EmailLogin, PasswordLogin, process_order
from logic.vacancy_list import VacancyList
from logic.vacancy import Vacancy
from time import sleep


def main() -> None:
    with create_driver() as driver:
        inputter = ConsoleInput()

        login_controls = LoginPage(driver)
        vacancy_list_page_controls = VacancyListPage(driver)
        vacancy_page_controls = VacancyPage(driver)

        email_method = EmailLogin(login_controls, inputter)
        password_method = PasswordLogin(login_controls, inputter)

        # process_order(email_method, password_method)

        vacancy_list = VacancyList(vacancy_list_page_controls, inputter)
        vacancy_controls = Vacancy(vacancy_page_controls, inputter)
        c = 0

        for link in vacancy_list.get_vacancy_links():
            vacancy_controls.goto_vacancy_page(link)

            # exiting the loop for testing purposes
            if c >= 100:
                break
            else:
                c += 1

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Shutting down')
