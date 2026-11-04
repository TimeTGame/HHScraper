from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class VacancyListPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.list_index = 1
        self.CARD_TITLE = (By.CSS_SELECTOR, "a[data-qa='serp-item__title']")
        self.NEXT_PAGE_BT = (By.CSS_SELECTOR, "a[data-qa='pager-next']")

    def goto_vacancy_list(self):
        self.driver.get('https://hh.ru/search/vacancy?text=&hhtmFrom=main&hhtmFromLabel=vacancy_search_line')
        self.driver.implicitly_wait(10)

    def find_card_links_on_page(self):
        elements = self.driver.find_elements(*self.CARD_TITLE)
        links = []

        for el in elements:
            links.append(el.get_attribute("href"))

        return links

    def goto_next_page(self):
        self.driver.find_element(*self.NEXT_PAGE_BT).click()