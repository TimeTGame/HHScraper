from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from page_controls.base_ctrls import BasePage


class VacancyListPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver
        self.page_index = 0
        self.CARD_TITLE = (By.CSS_SELECTOR, "a[data-qa='serp-item__title']")
        self.NEXT_PAGE_BT = (By.CSS_SELECTOR, "a[data-qa='pager-next']")

    def goto_vacancy_list(self, query: str = '') -> None:
        url = (
            'https://hh.ru/search/vacancy?'
            f'{query}'
            '&hhtmFrom=main'
            '&hhtmFromLabel=vacancy_search_line'
        )
        self.driver.get(url)

        self._dismiss_cookies_banner()
        sleep(10)

    def find_card_links_on_page(self) -> list[str]:
        elements = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.CARD_TITLE)
        )

        links = []
        for el in elements:
            href = el.get_attribute("href")
            if href and "hh.ru/vacancy/" in href:
                links.append(href)
                
        return links

    def goto_next_page(self) -> bool:
        try:
            self.page_index += 1
            self.goto_vacancy_list(f'page={self.page_index}')
            sleep(10)
            self._dismiss_cookies_banner()

            return True
        except NoSuchElementException:
            return False
