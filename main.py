import json
from http import HTTPStatus
import uvicorn
from fastapi import FastAPI, HTTPException, Depends, Query
from models.AppStatus import AppStatus
from models.User import User
from fastapi_pagination import Page, Params, paginate


app = FastAPI()

users: list[User] = []


@app.get("/status", status_code=HTTPStatus.OK)
def status() -> AppStatus:
    return AppStatus(users=bool(users))


@app.get("/api/users/{user_id}", status_code=HTTPStatus.OK)
def get_user(user_id: int) -> User:
    if user_id < 1:
        raise HTTPException(status_code=HTTPStatus.UNPROCESSABLE_ENTITY, detail="Invalid user id")
    if user_id > len(users):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found")
    return users[user_id - 1]


# @app.get("/api/users/", status_code=HTTPStatus.OK)
# def get_users() -> list[User]:
#     return users

@app.get("/api/users", status_code=HTTPStatus.OK, response_model=Page[User])
def get_users(params: Params = Depends()):
    return paginate(users, params)

# http://localhost:8000/api/users?page=2&size=5


if __name__ == "__main__":
    with open("users.json") as f:
        users = json.load(f)

    for user in users:
        User.model_validate(user)

    print("Users loaded")

    uvicorn.run(app, host="localhost", port=8000)










# if __name__ == "__main__":
#     import uvicorn
#
#     uvicorn.run(app, host="127.0.0.1", port=8000)
#
#     # uvicorn main:app --reload (запуск терминал)
