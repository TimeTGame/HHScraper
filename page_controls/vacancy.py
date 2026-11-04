from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from page_controls.base_ctrls import BasePage


class VacancyPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.driver = driver
        self.VACANCY_TITLE = (By.CSS_SELECTOR, "h1[id='vacancy-title'] span span")
        self.VACANCY_SALARY = (By.CSS_SELECTOR, "div[data-qa='vacancy-salary']")
        self.WORK_EXPERIENCE = (By.CSS_SELECTOR, "span[data-qa='vacancy-experience']")
        self.EMPLOYMENT_TYPE = (By.CSS_SELECTOR, "div[data-qa='common-employment-text'] div span dl dd")
        self.HIRING_FORMATS = (By.CSS_SELECTOR, "div[data-qa='vacancy-hiring-formats'] dl dd")
        self.WORK_SCHEDULE = (By.CSS_SELECTOR, "div[data-qa='work-schedule-by-days-text'] dl dd")
        self.WORK_FORMATS = (By.CSS_SELECTOR, "div[data-qa='work-formats-text'] dl dd")
        self.WORKING_HOURS = (By.CSS_SELECTOR, "div[data-qa='working-hours-text'] div span dl dd")
        self.COMPANY_NAME = (By.CSS_SELECTOR, "a[data-qa='vacancy-company-name'] span span span")
        self.VACANCY_DESC = (By.CSS_SELECTOR, "div[data-qa='vacancy-description']")
        self.APPLY_JOB_BT = (By.CSS_SELECTOR, "a[data-qa='vacancy-response-link-top']")

    def goto_vacancy_page(self, link: str) -> None:
        self.driver.get(link)

        self._dismiss_cookies_banner()

    def parse_title(self) -> str:
        return self.driver.find_element(*self.VACANCY_TITLE).text

    def parse_salary(self) -> str:
        try:
            return self.driver.find_element(*self.VACANCY_SALARY).text
        except NoSuchElementException:
            return 'Income level not specified'

    def parse_experience(self) -> str:
        return self.driver.find_element(*self.WORK_EXPERIENCE).text

    def parse_employment_type(self) -> str:
        return self.driver.find_element(*self.EMPLOYMENT_TYPE).text

    def parse_hiring_formats(self) -> str:
        try:
            return self.driver.find_element(*self.HIRING_FORMATS).text
        except NoSuchElementException:
            return 'Hire type not specified'

    def parse_work_schedule(self) -> str:
        try:
            return self.driver.find_element(*self.WORK_SCHEDULE).text
        except NoSuchElementException:
            return 'Work schedule not specified'

    def parse_working_hours(self) -> str:
        try:
            return self.driver.find_element(*self.WORKING_HOURS).text
        except NoSuchElementException:
            return 'Working hours not specified'

    def parse_work_formats(self) -> str:
        return self.driver.find_element(*self.WORK_FORMATS).text

    def parse_company_name(self) -> str:
        return self.driver.find_element(*self.COMPANY_NAME).text

    def parse_vacancy_desc(self) -> str:
        return self.driver.find_element(*self.VACANCY_DESC).text

    def apply_for_a_job(self) -> None:
        self.driver.find_element(*self.APPLY_JOB_BT).click()
