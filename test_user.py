import pytest
import requests

from http_client import HTTPClient
from regisrer_api import RegisterApi

BASE_URL = "https://reqres.in"
headers =  {'x-api-key': 'reqres-free-v1'}


@pytest.fixture
def register_api():
    http_client = HTTPClient(BASE_URL, headers)
    return RegisterApi(http_client)


def test_users_post_create(register_api):

    register_api.create_user(headers)

    register_api.check_user(headers)


