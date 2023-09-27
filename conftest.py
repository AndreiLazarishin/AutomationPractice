import pytest
from selenium import webdriver

from constants.base import BASE_URL
from pages.start_page import StartPage


@pytest.fixture(scope='function')
def start_page():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    driver.implicitly_wait(2)
    driver.maximize_window()
    # driver.switch_to.default_content()
    yield StartPage(driver)
    driver.close()


@pytest.fixture()
def elements_page():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    driver.implicitly_wait(1.5)
    yield StartPage(driver)
    driver.close()
