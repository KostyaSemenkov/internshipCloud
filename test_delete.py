import requests


class TestDelete:
    '''Проверка удаления обьекта'''
    url = 'https://jsonplaceholder.typicode.com/posts'
    data = {"id": 10}

    def test_delete(self):
        res = requests.delete(self.url, params=self.data)

        assert res.status_code == 404
        assert res.json() == {}


