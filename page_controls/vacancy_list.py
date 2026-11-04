from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from urllib.parse import quote
from time import sleep


class VacancyListPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.CARD_TITLE = (By.CSS_SELECTOR, "a[data-qa='serp-item__title']")
        self.NEXT_PAGE_BT = (By.CSS_SELECTOR, "a[data-qa='pager-next']")
        self.COOKIES_EL = (By.ID, "bottom-cookies-policy-informer")

    def _dismiss_cookies_banner(self) -> None:
        try:
            banner = self.driver.find_element(*self.COOKIES_EL)
            self.driver.execute_script("arguments[0].style.display='none';", banner)
        except NoSuchElementException:
            pass

    def goto_vacancy_list(self, query: str = '') -> None:
        encoded_query = quote(query)
        url = (
            'https://hh.ru/search/vacancy'
            f'?text={encoded_query}'
            '&hhtmFrom=main'
            '&hhtmFromLabel=vacancy_search_line'
        )
        self.driver.get(url)

        self._dismiss_cookies_banner()

    def find_card_links_on_page(self) -> list[str]:
        elements = self.driver.find_elements(*self.CARD_TITLE)

        links = []
        for el in elements:
            href = el.get_attribute("href")
            if href and "hh.ru/vacancy/" in href:
                links.append(href)
        return links

    def goto_next_page(self) -> bool:
        try:
            self.driver.find_element(*self.NEXT_PAGE_BT).click()
            sleep(5)
            self._dismiss_cookies_banner()

            return True
        except NoSuchElementException:
            return False
