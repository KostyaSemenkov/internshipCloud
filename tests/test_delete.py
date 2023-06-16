import vars
import requests
import allure


@allure.epic('Проверка метода delete')
class TestDelete:
    '''Проверка удаления обьекта'''

    @allure.description('Удаление первой записи')
    def test_delete(self):
        res = requests.delete(vars.url_1)
        assert res.status_code == 200
        assert res.json() == {}

    @allure.description('Удаление пустой записи')
    def test_empty_delete(self):
        res = requests.delete(vars.url,data=vars.data_101)
        assert res.status_code == 404
