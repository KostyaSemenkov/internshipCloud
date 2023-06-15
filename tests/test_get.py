import allure
import requests


@allure.epic('Проверка метода get')
class TestGet:
    '''Проверка 3 валидных и 1 невалидного запроса Get'''
    url = 'https://jsonplaceholder.typicode.com/posts'

    @allure.description('Запрос 2 записи')
    def test_get_2(self):
        body_expected = {
                "userId": 1,
                "id": 2,
                "title": "qui est esse",
                "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
        }
        payload = {"userId": 1, "id": 2}
        res = requests.get(self.url, params=payload)
        assert res.status_code == 200
        body_actual = res.json()
        assert body_actual[0] == body_expected

    @allure.description('Запрос 51 записи')
    def test_get_51(self):
        body_expected = {
            "userId": 6,
            "id": 51,
            "title": "soluta aliquam aperiam consequatur illo quis voluptas",
            "body": "sunt dolores aut doloribus\ndolore doloribus voluptates tempora et\ndoloremque et quo\ncum asperiores sit consectetur dolorem"
        }
        payload = {"userId": 6, "id": 51}
        res = requests.get(self.url, params=payload)
        assert res.status_code == 200
        body_actual = res.json()
        assert body_actual[0] == body_expected

    @allure.description('Запрос 100 записи')
    def test_get_100(self):
        body_expected = {
            "userId": 10,
            "id": 100,
            "title": "at nam consequatur ea labore ea harum",
            "body": "cupiditate quo est a modi nesciunt soluta\nipsa voluptas error itaque dicta in\nautem qui minus magnam et distinctio eum\naccusamus ratione error aut"
        }
        payload = {"userId": 10, "id": 100}
        res = requests.get(self.url, params=payload)
        assert res.status_code == 200
        body_actual = res.json()
        assert body_actual[0] == body_expected

    @allure.description('Запрос несуществующей записи')
    def test_get_102(self):
        res_len = len(requests.get(self.url).json()) # Вычисляем актуальную длину списка данных
        len_for_not_valid = str(res_len + 1) # Добавляем к длине списка данных еденицу, чтобы всегда был невалидный запрос
        res = requests.get(f'https://jsonplaceholder.typicode.com/posts/{len_for_not_valid}')
        assert res.status_code == 404
