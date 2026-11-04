import os
import sys

parent_dir = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')
)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

from page_controls.vacancy_list import VacancyListPage
from input_methods import InputMethod


class VacancyList():
    def __init__(self, controls: VacancyListPage, inputter: InputMethod):
        self.ctrl = controls
        self.inputter = inputter

    def next_page(self):
        self.ctrl.goto_next_page()

    def get_vacancy_link(self):
        while True:
            links = self.ctrl.find_card_links_on_page()

            if not links:
                break

            for link in links:
                yield link

            self.next_page()
        