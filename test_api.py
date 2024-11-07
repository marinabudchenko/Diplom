import requests


headers = {"X-API-KEY":"WGNKNP0-1PAMZ5D-NVBVDN9-MFV9CZB"}
base_url = "https://api.kinopoisk.dev/v1.4"

@allure.id("123")
@allure.story("Поиск фильма")
@allure.feature("READ")
@allure.title("Получение списка активных организаций")
@allure.description("Запрос организация с параметром active = true")
def test_search_movie():
    response = requests.get(f"{base_url}/movie/search?page=1&limit=10&query=Harry%20Potter%20and%20the%20Philosopher%27s%20Stone", headers=headers)
    assert response.status_code ==200
    assert "id" in response.text


@allure.id("SKYPRO-2")
@allure.story("Получение списка компаний")
@allure.feature("READ")
@allure.title("Получение списка активных организаций")
@allure.description("Запрос организация с параметром active = true")
def test_capital_letter():
    response = requests.get(f"{base_url}/movie/search?page=1&limit=10&query=Harry%20Potter%20and%20the%20Philosopher%27s%20Stone", headers=headers)
    assert response.status_code ==200
    assert "id" in response.text


@allure.id("SKYPRO-2")
@allure.story("Получение списка компаний")
@allure.feature("READ")
@allure.title("Получение списка активных организаций")
@allure.description("Запрос организация с параметром active = true")
def test_russian_name():
    response = requests.get(f"{base_url}", headers=headers)
    assert response.status_code ==200
    assert "id" in response.text





