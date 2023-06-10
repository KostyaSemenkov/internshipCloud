import requests

def test_delete():
    url = 'https://jsonplaceholder.typicode.com/posts/1'

    data = {
        "id": 1
        }
    res = requests.delete(url, params=data)

    assert res.status_code == 200
    assert res.json() == {}
