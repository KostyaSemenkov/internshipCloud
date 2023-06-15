import requests


class TestDelete:
    '''Проверка удаления обьекта'''
    url1 = 'https://jsonplaceholder.typicode.com/posts/1'
    # data = {"id": 10}
    url_101 = 'https://jsonplaceholder.typicode.com/posts/101'

    def test_delete(self):
        res = requests.delete(self.url1)
        assert res.status_code == 200
        assert res.json() == {}

    def test_empty_delete(self):
        res = requests.delete(self.url_101)
        assert res.status_code == 200
        assert res.json() == {}