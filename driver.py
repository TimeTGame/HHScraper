from selenium import webdriver
from selenium.webdriver.chrome.options import Options


my_options = Options()
my_options.page_load_strategy = 'none'
driver = webdriver.Chrome(options=my_options)
