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