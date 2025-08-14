from http import HTTPStatus
import pytest
import requests
from app.models.User import User


def test_status_ok(app_url):
    response = requests.get(f"{app_url}/status")
    assert response.status_code == HTTPStatus.OK


def test_status_true(app_url):
    response = requests.get(f"{app_url}/status").json()
    assert response['database'] is True, 'данные не загружены'
