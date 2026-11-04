from page_controls.vacancy import VacancyPage
from input_methods import InputMethod
from typing import Any


class Vacancy():
    def __init__(self, controls: VacancyPage, inputter: InputMethod):
        self.ctrl = controls
        self.inputter = inputter

    def goto_vacancy_page(self, link: str) -> None:
        self.ctrl._goto_new_window()
        self.ctrl.goto_vacancy_page(link)

    def parse_vacancy(self) -> dict[str, Any]:
        vacancy = {
            'title': self.ctrl.parse_title(),
            'salary': self.ctrl.parse_salary(),
            'experience': self.ctrl.parse_experience(),
            'employment_type': self.ctrl.parse_employment_type(),
            'hiring_formats': self.ctrl.parse_hiring_formats(),
            'work_schedule': self.ctrl.parse_work_schedule(),
            'working_hours': self.ctrl.parse_working_hours(),
            'work_formats': self.ctrl.parse_work_formats(),
            'company_name': self.ctrl.parse_company_name(),
            'description': self.ctrl.parse_vacancy_desc(),
        }
        self.ctrl._close_window()

        return vacancy