from requests import Response


class Checking:

    # Метод для проверки статус кода
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code, f"Провал! Статус код = {response.status_code}"
        print(f"Успешно! Статус код = {response.status_code}")