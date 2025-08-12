from http import HTTPStatus
import pytest
import requests
from app.models.User import User
page = 2
# size = 5


def total_users(users):
    users_ids = [user["id"] for user in users]
    total = len(users_ids)
    return total


@pytest.fixture
def users(app_url):
    response = requests.get(f"{app_url}/api/users/")
    assert response.status_code == HTTPStatus.OK
    return response.json()


def est_users_pagination_ok(app_url):
    response = requests.get(f"{app_url}/api/users?page=2&size=5")
    assert response.status_code == HTTPStatus.OK

    users1 = response.json()
    for user in users1["items"]:
        User.model_validate(user)


def est_users_pagination_total(app_url, users):
    response = requests.get(f"{app_url}/api/users?page=2&size=5")
    total = total_users(users['items'])
    print(total)
    assert response.json()["total"] == total


def est_users_pagination_page(app_url):

    response = requests.get(f"{app_url}/api/users?page=2&size=5")
    assert response.json()["page"] == page


def est_users_pagination_size(app_url):
    response = requests.get(f"{app_url}/api/users?page=2&size=5")
    assert response.json()["size"] == len(response.json()["items"])


def est_users_pagination_pages(app_url, users):
    response = requests.get(f"{app_url}/api/users??page=2&size=5")
    total = total_users(users['items'])
    assert response.json()["pages"] == total//len(response.json()["items"])+1