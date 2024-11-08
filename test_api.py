import requests
import allure

headers = {"X-API-KEY":"WGNKNP0-1PAMZ5D-NVBVDN9-MFV9CZB"}
base_url = "https://api.kinopoisk.dev/v1.4"

@allure.id("123")
@allure.story("Поиск фильма")
@allure.feature("GET")
@allure.title("Поиск фильма на английском языке")
@allure.description("Позитивная проверка")
def test_search_movie():
    response = requests.get(f"{base_url}/movie/search?page=1&limit=10&query=Harry%20Potter%20and%20the%20Philosopher%27s%20Stone", headers=headers)
    assert response.status_code ==200
    assert "id" in response.text


@allure.id("123")
@allure.story("Поиск фильма")
@allure.feature("GET")
@allure.title("Поиск фильма в верхнем регистре")
@allure.description("Позитивная проверка")
def test_capital_letter():
    response = requests.get(f"{base_url}/movie/search?page=1&limit=10&query=Harry%20Potter%20and%20the%20Philosopher%27s%20Stone", headers=headers)
    assert response.status_code ==200
    assert "id" in response.text


@allure.id("123")
@allure.story("Поиск фильма")
@allure.feature("GET")
@allure.title("Поиск фильма на русском языке")
@allure.description("Позитивная проверка")
def test_russian_name():
    response = requests.get(f"{base_url}/movie/search?page=1&limit=10&query=%D1%82%D0%B8%D1%82%D0%B0%D0%BD%D0%B8%D0%BA", headers=headers)
    assert response.status_code ==200
    assert "id" in response.text


@allure.id("123")
@allure.story("Поиск фильма")
@allure.feature("GET")
@allure.title("Поиск фильма из несуществующих слов")
@allure.description("Негативная проверка")
def test_nonexistent_name():
    response = requests.get(f"{base_url}/movie/search?page=1&limit=1&query=%20%20%20hymkhhj%2Clufifi%2Cf%2C", headers=headers)
    assert response.status_code ==200



@allure.id("123")
@allure.story("Поиск фильма")
@allure.feature("GET")
@allure.title("Поиск фильма по смайлику ")
@allure.description("Негативная проверка")
def test_smiley_name():
    response = requests.get(f"{base_url}/movie/search?page=1&limit=1&query=%20%20%20%F0%9F%99%82", headers=headers)
    assert response.status_code ==200






