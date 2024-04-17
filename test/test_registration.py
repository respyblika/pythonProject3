
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.registration_page import RegistrationPage


def test_registration_positive(driver):
    registration_page = RegistrationPage(driver)
    registration_page.open("https://arnypraht.com/register/")
    registration_page.register("ghjkj@mail.ru", "ghjhgj8j", "female", "+79656325687")
    WebDriverWait(driver, 10).until(EC.url_to_be("https://arnypraht.com/register/"))
    success_message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//*[@class=\"h4 h--subtitled\"]"))
    )
    success_message_text = success_message_element.text
    assert "Спасибо за регистрацию!" in success_message_text, "Регистрация была успешной"
