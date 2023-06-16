import allure
import requests


@allure.epic('Проверка метода post')
class TestPost():
    '''Проверка валидного запроса и 3 невалидных запросов'''
    url = 'https://jsonplaceholder.typicode.com/posts'
    data = {
        "userId": "11",
        "id": 101,
        "title": "testing post",
        "body": "body of post"
    }
    data_empty = {'id': 101}
    data_empty_on_exist = {'id': 1}

    @allure.description('Внесение новой записи')
    def test_valid_post(self):
        res = requests.post(self.url, data=self.data)
        assert res.status_code == 201
        assert res.json() == self.data

    @allure.description('Внесение пустой записи')
    def test_empty_post(self):
        res = requests.post(self.url)
        assert res.status_code == 201
        assert res.json() == self.data_empty

    @allure.description('Внесение пустой записи с параметром id')
    def test_empty_post_2(self):
        res = requests.post(self.url, data=self.data_empty)
        assert res.status_code == 201
        assert res.json() == self.data_empty

    @allure.description('Внесение пустой записи с параметром id поверх уже существующей записи')
    def test_empty_on_exist(self):
        res = requests.post(self.url, data=self.data_empty_on_exist)
        assert res.status_code == 201
        assert  not res.json() == self.data_empty_on_exist