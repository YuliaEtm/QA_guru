# класс методов api
from symtable import Class

import requests

class RegisterApi:
    def __init__(self):
        self.base_url = "https://reqres.in"
        # BASE_URL = "https://reqres.in"
        self.headers = {'x-api-key': 'reqres-free-v1'}


def check_user(self):
    response = requests.get(f"{BASE_URL}/api/users/2", headers=headers)
    assert response.status_code == 200
    body = response.json()['data']
    print(body)
    assert body['first_name'] == "Janet"


def create_user(self):
    payload = {
        "name": "morpheus",
        "job": "leader"
    }
    response = requests.post(f"{BASE_URL}/api/users", json=payload, headers=headers)
    print(response.text)
    assert response.status_code in (200, 201)

    # {"data":{"id":2,"email":"janet.weaver@reqres.in","first_name":"Janet","last_name":"Weaver",
    # "avatar":"https://reqres.in/img/faces/2-image.jpg"},
    # "support":{"url":"https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral",
    # "text":"Tired of writing endless social media content? Let Content Caddy generate it for you."}}