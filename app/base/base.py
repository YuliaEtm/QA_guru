from http import HTTPStatus
from sqlmodel import SQLModel, Session, select
from pydantic import BaseModel
import requests


class Base(SQLModel):
    def __init__(self, base_url):
        super.session = requests.session()
        super.base_url = base_url


    def get_list_users(app_url):
        response = requests.get(f"{app_url}/api/users/")
        assert response.status_code == HTTPStatus.OK
        return response
