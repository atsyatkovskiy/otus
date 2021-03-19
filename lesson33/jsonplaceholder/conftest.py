import pytest
import requests
from methods import APIClient


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://jsonplaceholder.typicode.com/",
        help="Введите url"
    )


@pytest.fixture(scope="session")
def api_client(request):
    base_url = request.config.getoption("--url")
    return APIClient(base_url=base_url)