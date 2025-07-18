import requests

url = "https://reqres.in/api"
headers = {'x-api-key': 'reqres-free-v1'}


def test_post_greate_user():
    param = "users"
    response = requests.post(f'{url}/{param}', headers=headers, data={"name": "Вася", "job": "кот"})
    body = response.json()
    print(body)
    # {'name': 'Вася', 'job': 'кот', 'id': '603', 'createdAt': '2025-07-17T14:09:35.135Z'}
    assert response.status_code == 201
    assert body['name'] == "Вася"
    assert body['job'] == "кот"


def test_get_single_user():
    param = "users/10"
    payload = {"id": 10,
               "email": "byron.fields@reqres.in",
               "first_name": "Byron",
               "last_name": "Fields",
               "avatar": "https://reqres.in/img/faces/10-image.jpg"}
    response = requests.get(f'{url}/{param}', headers=headers)
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
    param = "users/2"
    response = requests.delete(f'{url}/{param}', headers=headers)
    assert response.status_code == 204


def test_get_users_returns_unique_users():
    param = "unknown"
    response = requests.get(f'{url}/{param}', headers=headers)
    assert response.status_code == 200
    body = response.json()
    assert body['per_page'] == len(body['data'])
