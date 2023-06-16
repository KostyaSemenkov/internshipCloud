import allure
import requests
import vars

@allure.epic('Проверка метода post')
class TestPost():
    '''Проверка валидного запроса и 3 невалидных запросов'''

    @allure.description('Внесение новой записи')
    def test_valid_post(self):
        res = requests.post(vars.url, data=vars.body_101)
        assert res.status_code == 201
        assert res.json() == vars.body_101

    @allure.description('Внесение пустой записи')
    def test_empty_post(self):
        res = requests.post(vars.url)
        assert res.status_code == 201
        assert res.json() == vars.data_empty

    @allure.description('Внесение пустой записи с параметром id')
    def test_empty_post_2(self):
        res = requests.post(vars.url, data=vars.data_empty)
        assert res.status_code == 201
        assert res.json() == vars.data_empty

    @allure.description('Внесение пустой записи с параметром id поверх уже существующей записи')
    def test_empty_on_exist(self):
        res = requests.post(vars.url, data=vars.data_empty_on_exist)
        assert res.status_code == 201
        assert  not res.json() == vars.data_empty_on_exist