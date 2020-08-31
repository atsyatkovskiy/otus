import pytest
import requests


class APIClient:

    def __init__(self, base_address):
        self.base_address = base_address

    def custom(self, method, path="/", **kwargs):
        url = self.base_address + path
        return requests.request(method, url=url, **kwargs)

    def get(self, path="/", params=None):
        url = self.base_address + path
        return requests.get(url=url, params=params)


def pytest_addoption(parser):
    parser.addoption("--url", default="https://api.openbrewerydb.org")


@pytest.fixture()
def api_client(request):
    base_url = request.config.getoption("--url")
    return APIClient(base_address=base_url)
