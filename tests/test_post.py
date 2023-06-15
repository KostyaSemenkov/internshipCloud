import allure
import requests


@allure.epic('Проверка метода post')
class TestPost():
    '''Проверка валидного запроса и запроса с пустым body'''
    url = 'https://jsonplaceholder.typicode.com/posts'
    data = {
        "userId": "11",
        "id": 101,
        "title": "testing post",
        "body": "body of post"
    }
    data_empty = {'id': 101}

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

