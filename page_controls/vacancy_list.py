from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from urllib.parse import quote


class VacancyListPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.CARD_TITLE = (By.CSS_SELECTOR, "a[data-qa='serp-item__title']")
        self.NEXT_PAGE_BT = (By.CSS_SELECTOR, "a[data-qa='pager-next']")

    def goto_vacancy_list(self, query: str = '') -> None:
        encoded_query = quote(query)
        url = (
            'https://hh.ru/search/vacancy'
            f'?text={encoded_query}'
            '&hhtmFrom=main'
            '&hhtmFromLabel=vacancy_search_line'
        )
        self.driver.get(url)

    def find_card_links_on_page(self) -> list[str]:
        elements = self.driver.find_elements(*self.CARD_TITLE)

        return [el.get_attribute("href") for el in elements]

    def goto_next_page(self) -> bool:
        try:
            self.driver.find_element(*self.NEXT_PAGE_BT).click()
            return True
        except NoSuchElementException:
            return False
