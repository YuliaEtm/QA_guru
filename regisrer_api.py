# класс методов api
from symtable import Class

import requests

from http_client import HTTPClient


class RegisterApi:
    def __init__(self, http_client: HTTPClient):
        self.http_client = http_client
        self.headers = {'x-api-key': 'reqres-free-v1'}

    def check_user(self, headers):
        response = self.http_client.get(path='/api/users/2', headers=headers)
        assert response.status_code == 200
        body = response.json()['data']
        print(body)
        assert body['first_name'] == "Janet"
        return response

    def create_user(self, headers):
        payload = {
            "name": "morpheus",
            "job": "leader"
        }
        response = self.http_client.post(path="/api/users", json=payload, headers={'x-api-key': 'reqres-free-v1'})
        print(response.text)
        # assert response.status_code in (200, 201)
        return response

        # {"data":{"id":2,"email":"janet.weaver@reqres.in","first_name":"Janet","last_name":"Weaver",
        # "avatar":"https://reqres.in/img/faces/2-image.jpg"},
        # "support":{"url":"https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral",
        # "text":"Tired of writing endless social media content? Let Content Caddy generate it for you."}}
