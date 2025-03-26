from utils.http_methods import HTTPMethods


base_url = "https://rahulshettyacademy.com"
key = "?key=qaclick123"

class GoogleMapsApi:

    # Метод создания локации
    @staticmethod
    def create_new_place():

        json_for_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
             ],
             "website": "http://google.com",
            "language": "French-IN"
        }

        # Формирование URL запроса
        post_resource = "/maps/api/place/add/json"
        post_url = base_url + post_resource + key
        print(post_url)

        # Отправка запроса метода POST
        result_post = HTTPMethods.post(post_url, json_for_create_new_place)
        print(result_post.json())
        return result_post

    # Метод поиска локации
    @staticmethod
    def get_new_place(place_id):

        # Формирование URL запроса
        get_resource = "/maps/api/place/get/json"
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)

        # Отправка GET запроса
        result_get = HTTPMethods.get(get_url)
        print(result_get.json())
        return result_get

    @staticmethod
    def put_new_place(place_id):

        # Формирование URL запроса
        put_resource = "/maps/api/place/update/json"
        put_url = base_url + put_resource + key
        print(put_url)

        json_for_update_location = {
            "place_id" : place_id,
            "address" : "100 Lenina street, RU",
            "key" : "qaclick123"
        }

        # Отправка PUT запроса
        result_put = HTTPMethods.put(put_url, json_for_update_location)
        print(result_put.json())
        return result_put

    @staticmethod
    def delete_new_place(place_id):

        # Формирование URL запроса
        delete_resource = "/maps/api/place/delete/json"
        delete_url = base_url + delete_resource + key
        print(delete_url)
        json_for_delete_location = {
             "place_id" : place_id
        }

        # Отправка запроса на удаление
        result_delete = HTTPMethods.delete(delete_url, json_for_delete_location)
        print(result_delete.json())
        return result_delete