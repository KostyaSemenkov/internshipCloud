import allure
import requests
import vars

@allure.epic('Проверка метода get')
class TestGet:
    '''Проверка 4 валидных и 1 невалидного запроса Get'''

    @allure.description('Запрос 2 записи')
    def test_get_2(self):
        res = requests.get(vars.url, params=vars.payload_2)
        assert res.status_code == 200
        actual_body = res.json()
        assert actual_body[0] == vars.expected_body_2

    @allure.description('Запрос 51 записи')
    def test_get_51(self):
        res = requests.get(vars.url, params=vars.payload_51)
        assert res.status_code == 200
        actual_body = res.json()
        assert actual_body[0] == vars.expected_body_51

    @allure.description('Запрос 100 записи')
    def test_get_100(self):
        res = requests.get(vars.url, params=vars.payload_100)
        assert res.status_code == 200
        actual_body = res.json()
        assert actual_body[0] == vars.expected_body_100

    @allure.description('Запрос несуществующей записи')
    def test_get_102(self):
        res_len = len(requests.get(vars.url).json()) # Вычисляем актуальную длину списка данных
        len_for_not_valid = str(res_len + 1) # Добавляем к длине списка данных еденицу, чтобы всегда был невалидный запрос
        res = requests.get(f'https://jsonplaceholder.typicode.com/posts/{len_for_not_valid}')
        assert res.status_code == 404

    @allure.description('Запрос всех записей и проверка количества записей')
    def test_get_all(self):
        res = requests.get(vars.url)
        assert res.status_code == 200
        actual_body = res.json()
        assert actual_body == vars.expected_body_all
        assert len(actual_body) == 100
