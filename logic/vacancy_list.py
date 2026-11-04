from page_controls.vacancy_list import VacancyListPage
from input_methods import InputMethod
from typing import Iterator


class VacancyList():
    def __init__(self, controls: VacancyListPage, inputter: InputMethod):
        self.ctrl = controls
        self.inputter = inputter

    def get_vacancy_links(self, query: str = '') -> Iterator[str]:
        self.ctrl.goto_vacancy_list(query)

        while True:
            links = self.ctrl.find_card_links_on_page()

            if not links:
                break

            yield from links

            if not self.ctrl.goto_next_page():
                break
        