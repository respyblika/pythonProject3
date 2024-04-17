import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)

    yield driver
    driver.quit()
