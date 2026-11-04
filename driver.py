from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def create_driver() -> webdriver.Chrome:
    my_options = Options()
    my_options.page_load_strategy = 'none'

    driver = webdriver.Chrome(options=my_options)
    driver.implicitly_wait(10)

    return driver
