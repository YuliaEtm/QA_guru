import requests

url = "https://reqres.in/api/users"
headers = {'x-api-key': 'reqres-free-v1'}


def test_post_greate_user():
    response = requests.post(url, headers=headers, data={"name": "Вася", "job": "кот"})
    body = response.json()
    print(body)
    # {'name': 'Вася', 'job': 'кот', 'id': '603', 'createdAt': '2025-07-17T14:09:35.135Z'}
    assert response.status_code == 201
    assert body['name'] == "Вася"
    assert body['job'] == "кот"


def test_get_single_user():
    payload = {"id": 10,
               "email": "byron.fields@reqres.in",
               "first_name": "Byron",
               "last_name": "Fields",
               "avatar": "https://reqres.in/img/faces/10-image.jpg"}
    response = requests.get("https://reqres.in/api/users/10", headers=headers)
    assert response.status_code == 200
    body = response.json()['data']
    print(body)
    # {'id': 10, 'email': 'byron.fields@reqres.in', 'first_name': 'Byron', 'last_name': 'Fields', 'avatar':
    # 'https://reqres.in/img/faces/10-image.jpg'}
    assert body['id'] == 10
    assert body['email'] == payload['email']
    assert body['first_name'] == payload['first_name']
    assert body['last_name'] == payload['last_name']


def test_delete_user():
    response = requests.delete("https://reqres.in/api/users/2", headers=headers)
    assert response.status_code == 204


def test_get_users_returns_unique_users():
    response = requests.get(url="https://reqres.in/api/unknown", headers=headers)
    assert response.status_code == 200
    body = response.json()
    assert body['per_page'] == len(body['data'])
