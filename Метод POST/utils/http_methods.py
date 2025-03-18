import requests

# Класс методов API
class HTTPMethods:
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    # Метод GET
    @staticmethod
    def get(url):
        result = requests.get(url, headers=HTTPMethods.headers, cookies=HTTPMethods.cookie)
        return result

    # Метод POST
    @staticmethod
    def post(url, body):
        result = requests.post(url, json=body, headers=HTTPMethods.headers, cookies=HTTPMethods.cookie)
        return result

    # Метод PUT
    @staticmethod
    def put(url, body):
        result = requests.put(url, json=body, headers=HTTPMethods.headers, cookies=HTTPMethods.cookie)
        return result

    # Метод DELETE
    @staticmethod
    def delete(url, body):
        result = requests.delete(url, json=body, headers=HTTPMethods.headers, cookies=HTTPMethods.cookie)
        return result