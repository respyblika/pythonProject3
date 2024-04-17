import time
from pages.login_page import LoginPage

def test_login_positive(driver):
    login_page = LoginPage(driver)
    login_page.open("https://arnypraht.com/login/")
    login_page.login("valerya12002@mail.ru", "12345678")
    time.sleep(5)
    expected_url = "https://arnypraht.com/account/overview/"
    actual_url = login_page.get_current_url()
    assert actual_url == expected_url, f"Провалено"