import pytest
import paramiko

client = paramiko.SSHClient()


def ssh_connect():
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(
        hostname="localhost",
        username="root",
        password="12345678",
        port=22
    )


def ssh_close():
    client.close()


def pytest_addoption(parser):
    parser.addoption("--name_opencart", action="store", default="docker_opencart_1")
    parser.addoption("--name_db", action="store", default="docker_mariadb_1")


@pytest.fixture
def param_name_opencart(request):
    name_opencart = request.config.getoption('--name_opencart')
    return name_opencart


@pytest.fixture
def param_name_db(request):
    name_db = request.config.getoption('--name_db')
    return name_db
