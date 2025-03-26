import json
from requests import Response


class Checking:

    # Метод для проверки статус кода
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code, f"Провал! Статус код = {response.status_code}"
        print(f"Успешно! Статус код = {response.status_code}")

    # Метод проверки наличия полей
    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value, 'Провал! Некоторые поля отсутствуют!'
        print('Все поля присутствуют')

    # Метод сравнения значения поля
    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value, field_name + 'не верен.'
        print(field_name + ' верен.')

    # Метод поиска слова в значении поля
    @staticmethod
    def check_json_search_word_in_value(response: Response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        assert search_word in check_info, 'Слово ' + search_word + ' отсутствует.'
        print('Слово ' + search_word + ' присутствует.')