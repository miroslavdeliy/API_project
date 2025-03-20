from requests import  Response
from utils.api import GoogleMapsApi


class TestCreatePlace:
    # Метод тестирования создания локации
    def test_create_new_place(self):

        # Шаг теста для метода POST
        print('Метод POST')
        result_post: Response = GoogleMapsApi.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get('place_id')

        # Шаг теста GET для проверки отработки POST
        print('Метод GET POST')
        result_get: Response = GoogleMapsApi.get_new_place(place_id)

        # Шаг теста для метода PUT
        print('Метод PUT')
        result_put: Response = GoogleMapsApi.put_new_place(place_id)

        # Шаг теста GET для проверки отработки PUT
        print('Метод GET PUT')
        result_get: Response = GoogleMapsApi.get_new_place(place_id)

        # Шаг теста для метода DELETE
        print('Метод DELETE')
        result_delete: Response = GoogleMapsApi.delete_new_place(place_id)

        # Шаг теста GET для проверки отработки PUT
        print('Метод GET DELETE')
        result_get: Response = GoogleMapsApi.get_new_place(place_id)
