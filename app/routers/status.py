from http import HTTPStatus

from fastapi import APIRouter
# from app.routers.database import users_db
# from app.database.engine import check_availability
from app.models.AppStatus import AppStatus


router = APIRouter()


@router.get("/status", status_code=HTTPStatus.OK)
def status() -> AppStatus:
    # return AppStatus(database=check_availability())
    return AppStatus(users=True)
