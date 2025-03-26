import requests
from utils.logger import Logger


# Класс методов API
class HTTPMethods:
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    # Метод GET
    @staticmethod
    def get(url):
        Logger.add_request(url, method='GET')
        result = requests.get(url, headers=HTTPMethods.headers, cookies=HTTPMethods.cookie)
        Logger.add_response(result)
        return result

    # Метод POST
    @staticmethod
    def post(url, body):
        Logger.add_request(url, method='POST')
        result = requests.post(url, json=body, headers=HTTPMethods.headers, cookies=HTTPMethods.cookie)
        Logger.add_response(result)
        return result

    # Метод PUT
    @staticmethod
    def put(url, body):
        Logger.add_request(url, method='PUT')
        result = requests.put(url, json=body, headers=HTTPMethods.headers, cookies=HTTPMethods.cookie)
        Logger.add_response(result)
        return result

    # Метод DELETE
    @staticmethod
    def delete(url, body):
        Logger.add_request(url, method='DELETE')
        result = requests.delete(url, json=body, headers=HTTPMethods.headers, cookies=HTTPMethods.cookie)
        Logger.add_response(result)
        return result