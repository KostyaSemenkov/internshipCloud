import  requests


def test_post():
    url = 'https://jsonplaceholder.typicode.com/posts'
    data = {
        "userId": 11,
        "id": 101,
        "title": "testing post",
        "body": "body of post"
         }
    res = requests.post(url, data=data)
    print(res.json())
    assert res.status_code == 201
    assert res.json() == data