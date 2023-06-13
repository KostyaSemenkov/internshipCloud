import requests
import  pytest


class TestGet:
    url = 'https://jsonplaceholder.typicode.com/posts'

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