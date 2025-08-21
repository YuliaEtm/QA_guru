import dotenv
import pytest
from tests.utils.base_session import BaseSession
from tests.utils.config import Server





# @pytest.fixture(scope="session", autouse=True)
# def envs():
#     dotenv.load_dotenv()


# def pytest_addoption(parser):
#     parser.addoption("--env", default="dev")


# @pytest.fixture(scope="session")
# def env(request):
#     return request.config.getoption("--env")


# @pytest.fixture(scope="module")
# def user_factory():
#     return UserFactory()


@pytest.fixture(scope='session')
def user_client():
    with BaseSession(base_url=f"http://127.0.0.1:8000") as session:
        yield session


@pytest.fixture(scope='session')
def status_client(env):
    with BaseSession(base_url=f"{Server(env).user_service}/status") as session:
        yield session
