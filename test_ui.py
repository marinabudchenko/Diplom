import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()

    browser.implicitly_wait(40)
    yield browser
    browser.quit()

@allure.title("Поиск фильма по названию")
@allure.description("Вводим валидные данные")
@allure.epic("UI тесты")
@allure.story("Поиск")
@allure.feature("Позитивные тесты")
@allure.severity("blocker")
@pytest.mark.parametrize("name", [    ("Хоббит"),
    ("преступление и наказание"),    ("1+1"),
    ("И снова здравствуйте!")])
def test_search_possitive(driver, name):
    driver.get("https://www.kinopoisk.ru/")
    driver.find_element(By.CSS_SELECTOR, "input[name=kp_query]").send_keys(name)
    driver.find_element(By.CSS_SELECTOR, "button.styles_root__CUh_v").click()
    div = driver.find_element(By.CSS_SELECTOR, "div.info")
    title = div.find_element(By.CSS_SELECTOR, "p.name")
    with allure.step("Сравнить название фильма с полученным"):
        assert name.lower() in title.text.lower()
