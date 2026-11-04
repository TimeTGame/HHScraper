from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class BasePage():
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.main_window = ''
        self.COOKIES_EL = (By.ID, "bottom-cookies-policy-informer")

    def _dismiss_cookies_banner(self) -> None:
        try:
            banner = self.driver.find_element(*self.COOKIES_EL)
            self.driver.execute_script("arguments[0].style.display='none';", banner)
        except NoSuchElementException:
            pass

    def _goto_new_window(self) -> None:
        self.main_window = self.driver.current_window_handle
        self.driver.switch_to.new_window('tab')

    def _close_window(self) -> None:
        self.driver.close()
        self.driver.switch_to.window(self.main_window)
