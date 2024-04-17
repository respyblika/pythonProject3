import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.search_page import SearchPage

def test_search_positive(driver):
    search_page = SearchPage(driver)
    search_page.open("https://arnypraht.com/login/")
    tovar = "юбки"
    search_page.search("valerya12002@mail.ru", "12345678", tovar)
    time.sleep(10)
    email_link = WebDriverWait(driver, 10).until(
     EC.visibility_of_element_located((By.XPATH, "//*[@class=\"search-form__info\"]/span"))
    )
    assert email_link.text == "По запросу " + tovar, f"Failed"