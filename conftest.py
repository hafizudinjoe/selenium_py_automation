import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from settings import INIT_MOVE_X, WAIT_QUIT, CHROME_DRIVER


@pytest.fixture
def fresh_browser():
    service = Service(executable_path=CHROME_DRIVER)
    driver = webdriver.Chrome(service=service)
    driver.set_window_position(INIT_MOVE_X, 0)
    driver.maximize_window()
    yield driver
    time.sleep(WAIT_QUIT)
    driver.quit()


@pytest.fixture(scope='module')
def same_browser():
    service = Service(executable_path=CHROME_DRIVER)
    driver = webdriver.Chrome(service=service)
    driver.set_window_position(INIT_MOVE_X, 0)
    driver.maximize_window()
    yield driver
    time.sleep(WAIT_QUIT)
    driver.quit()


@pytest.fixture
def headless_browser():
    service = Service(executable_path=CHROME_DRIVER)
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_window_position(INIT_MOVE_X, 0)
    driver.maximize_window()
    yield driver
    driver.quit()
