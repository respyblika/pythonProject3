import time
from pages.navigation_page import NavigationPage

def test_navigation_positive(driver):
    navigation_page = NavigationPage(driver)
    navigation_page.open("https://arnypraht.com/login/")
    navigation_page.navigation("valerya12002@mail.ru", "12345678")
    time.sleep(5)
    expected_url = "https://arnypraht.com/cart/"
    actual_url = navigation_page.get_current_url()
    assert actual_url == expected_url, f"Выполнено"