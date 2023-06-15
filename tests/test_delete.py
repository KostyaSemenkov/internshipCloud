import requests
import allure


@allure.epic('Проверка метода delete')
class TestDelete:
    '''Проверка удаления обьекта'''
    url1 = 'https://jsonplaceholder.typicode.com/posts/1'
    # data = {"id": 10}
    url_101 = 'https://jsonplaceholder.typicode.com/posts/101'

    @allure.description('Удаление первой записи')
    def test_delete(self):
        res = requests.delete(self.url1)
        assert res.status_code == 200
        assert res.json() == {}

    @allure.description('Удаление пустой записи записи')
    def test_empty_delete(self):
        res = requests.delete(self.url_101)
        assert res.status_code == 200
        assert res.json() == {}