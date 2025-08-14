import json
from http import HTTPStatus

import pytest
import requests
from app.models.User import User


@pytest.fixture(scope="module")
def fill_test_data(app_url):
    with open("users.json") as f:
        test_data_users = json.load(f)
    api_users = []
    for user in test_data_users:
        response = requests.post(f"{app_url}/api/users/", json=user)
        api_users.append(response.json())

    user_ids = [user["id"] for user in api_users]

    yield user_ids

    for user_id in user_ids:
        requests.delete(f"{app_url}/api/users/{user_id}")
from models.User import User


@pytest.fixture
def users(app_url):
    response = requests.get(f"{app_url}/api/users/")
    assert response.status_code == HTTPStatus.OK
    return response.json()


@pytest.mark.usefixtures("fill_test_data")
def test_users(app_url):
    response = requests.get(f"{app_url}/api/users/")
    assert response.status_code == HTTPStatus.OK

    user_list = response.json()
    for user in user_list:
    users1 = response.json()
    for user in users1:
        User.model_validate(user)


@pytest.mark.usefixtures("fill_test_data")
def test_users_no_duplicates(users):
    users_ids = [user["id"] for user in users]
    assert len(users_ids) == len(set(users_ids))


def test_user(app_url, fill_test_data):
    for user_id in (fill_test_data[0], fill_test_data[-1]):
        response = requests.get(f"{app_url}/api/users/{user_id}")
        assert response.status_code == HTTPStatus.OK
        user = response.json()
        User.model_validate(user)
@pytest.mark.parametrize("user_id", [1, 6, 12])
def test_user(app_url, user_id):
    response = requests.get(f"{app_url}/api/users/{user_id}")
    assert response.status_code == HTTPStatus.OK

    user = response.json()
    User.model_validate(user)


@pytest.mark.parametrize("user_id", [13])
def test_user_nonexistent_values(app_url, user_id):
    response = requests.get(f"{app_url}/api/users/{user_id}")
    assert response.status_code == HTTPStatus.NOT_FOUND



@pytest.mark.parametrize("user_id", [-1, 0, "word"])
def test_user_invalid_values(app_url, user_id):
    response = requests.get(f"{app_url}/api/users/{user_id}")
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_new_user(app_url, fill_test_data):
    # Создаем нового пользователя
    payload = {
        "email": "dog.cat@reqres.in",
        "first_name": "Киса",
        "last_name": "Сабакевич",
        "avatar": "https://reqres.in/img/faces/15-image.jpg"
        }
    response = requests.post(f"{app_url}/api/users", json=payload)
    user_id = response.json()['id']
    assert response.status_code == HTTPStatus.CREATED

    deleted_user = requests.delete(f"{app_url}/api/users/{user_id}")
    assert deleted_user.status_code == HTTPStatus.OK


def test_new_user_fild(app_url, fill_test_data):
    # Создаем нового пользователя и проверяем поля
    payload = {
        "email": "cat.dog@reqres.in",
        "first_name": "Собак",
        "last_name": "Кисович",
        "avatar": "https://reqres.in/img/faces/26-image.jpg"
        }
    response = requests.post(f"{app_url}/api/users", json=payload)
    assert response.status_code == HTTPStatus.CREATED

    user_id = response.json()['id']
    new_user = requests.get(f"{app_url}/api/users/{user_id}").json()

    # {'id': 224, 'email': 'cat.dog@reqres.in', 'last_name': 'Кисович', 'first_name': 'Собак',
    # 'avatar': 'https://reqres.in/img/faces/26-image.jpg'}
    assert new_user['email'] == payload['email']
    assert new_user['last_name'] == payload['last_name']
    assert new_user['first_name'] == payload['first_name']
    assert new_user['avatar'] == payload['avatar']

    deleted_user = requests.delete(f"{app_url}/api/users/{user_id}")
    assert deleted_user.status_code == HTTPStatus.OK

def test_delete_user(app_url, fill_test_data):
    # Создаем и удаляем нового пользователя
    payload = {
        "email": "red.cat@reqres.in",
        "first_name": "Рыжий",
        "last_name": "Лис",
        "avatar": "https://reqres.in/img/faces/55-image.jpg"
        }
    response = requests.post(f"{app_url}/api/users", json=payload)

    user_id = response.json()['id']

    deleted_user = requests.delete(f"{app_url}/api/users/{user_id}")
    assert deleted_user.status_code == HTTPStatus.OK


def test_delete_user404(app_url, fill_test_data):
    # Создаем и удаляем нового пользователя, проверяем удаление
    payload = {
        "email": "black.cat@reqres.in",
        "first_name": "Black",
        "last_name": "Cat",
        "avatar": "https://reqres.in/img/faces/27-image.jpg"
        }
    response = requests.post(f"{app_url}/api/users", json=payload)

    user_id = response.json()['id']

    deleted_user = requests.delete(f"{app_url}/api/users/{user_id}")
    assert deleted_user.status_code == HTTPStatus.OK

    response = requests.get(f"{app_url}/api/users/{user_id}")
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_patch_user(app_url, fill_test_data):
    # Создаем и изменяем нового пользователя
    payload = {
        "email": "white.dog@reqres.in",
        "first_name": "White",
        "last_name": "Dog",
        "avatar": "https://reqres.in/img/faces/29-image.jpg"
        }
    response = requests.post(f"{app_url}/api/users", json=payload)

    user_id = response.json()['id']

    data = {"last_name": "Cat"}

    requests.patch(f"{app_url}/api/users/{user_id}", json=data)
    patch_user = requests.get(f"{app_url}/api/users/{user_id}").json()
    print(patch_user)
    # {'id': 224, 'email': 'cat.dog@reqres.in', 'last_name': 'Кисович', 'first_name': 'Собак',
    # 'avatar': 'https://reqres.in/img/faces/26-image.jpg'}
    assert patch_user['email'] == payload['email']
    assert patch_user['last_name'] == data['last_name']
    assert patch_user['first_name'] == payload['first_name']
    assert patch_user['avatar'] == payload['avatar']

    deleted_user = requests.delete(f"{app_url}/api/users/{user_id}")
    assert deleted_user.status_code == HTTPStatus.OK


# def test_aaa(app_url):
#     users_ids = (118/119)
#     for user_id in range(900, 1000):
#         deleted_user = requests.delete(f"{app_url}/api/users/{user_id}")
