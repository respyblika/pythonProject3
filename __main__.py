from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.search_page import SearchPage
from test.conftest import driver
from test.test_basket import test_basket_positive
from test.test_editing_basket import test_editing_positive
from test.test_search import test_search_positive

s = Service(ChromeDriverManager().install())
    # Initialize the Chrome WebDriver with the service
driver = webdriver.Chrome(service=s)
driver1 = webdriver.Chrome(service=s)

test_editing_positive(driver)
driver.quit()
test_basket_positive(driver1)
driver1.quit()

