import requests


class TestPost():

    url = 'https://jsonplaceholder.typicode.com/posts'
    data = {
        "userId": "11",
        "id": 101,
        "title": "testing post",
        "body": "body of post"
    }
    data_empty = {'id': 101}

    def test_valid_post(self):
        res = requests.post(self.url, data=self.data)
        assert res.status_code == 201
        assert res.json() == self.data

    def test_empty_post(self):
        res = requests.post(self.url)
        assert res.status_code == 201
        assert res.json() == self.data_empty


