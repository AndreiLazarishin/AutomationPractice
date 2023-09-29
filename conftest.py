import pytest
from selenium import webdriver

from constants.base import BASE_URL
from pages.start_page import StartPage


@pytest.fixture(scope='function')
def start_page():
    from selenium.webdriver.chrome.options import Options
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    driver.implicitly_wait(2)
    driver.maximize_window()
    yield StartPage(driver)
    driver.close()


@pytest.fixture()
def elements_page():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    driver.implicitly_wait(1.5)
    yield StartPage(driver)
    driver.close()
