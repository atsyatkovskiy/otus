import pytest
from selenium.webdriver import ChromeOptions, FirefoxOptions, IeOptions
import logging
from selenium import webdriver
import os

#cwd = os.getcwd()  # Get the current working directory (cwd)
#files = os.listdir(cwd)  # Get all the files in that directory
#print("Files in %r: %s" % (cwd, files))

logging.basicConfig(level=logging.INFO, filename="logs\\selenium.log")


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome", help="Please, choose your browser")
    parser.addoption("--url", "-U", action="store", default="https://localhost/admin/")


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request, url):
    # Сбор параметров запуска для pytest
    browser = request.config.getoption("--browser")
    logger = logging.getLogger('BrowserLogger')
    test_name = request.node.name
    logger.info("===> Test {} started".format(test_name))

    """ Инициализация браузера """
    if browser == "chrome":
        #  driver = webdriver.Chrome(executable_path=drivers + "/chromedriver")
        option = ChromeOptions()
        option.add_argument('--disable-popup-blocking')
        option.add_argument('--ignore-certificate-errors')
        # option.add_argument('--headless')
        driver = webdriver.Chrome(options=option)
    elif browser == "firefox":
        option = FirefoxOptions()
        option.add_argument('--headless')
        driver = webdriver.Firefox(options=option)
        #  driver = webdriver.Firefox(executable_path=drivers + "/geckodriver")
    elif browser == "ie":
        option = IeOptions()
        option.add_argument('--headless')
        driver = webdriver.Ie(options=option)
        #  driver = webdriver.Opera(executable_path=drivers + "/iedriver")
    else:
        raise Exception(f"{request.param} is not supported!")
    # Предварительная настройка запуска
    driver.maximize_window()
    logger.info("Browser {} started with {}".format(browser, driver.desired_capabilities))

    def fin():
        driver.quit()
        logger.info("Browser {} closed".format(browser))
        logger.info("===> Test {} FINISHED".format(test_name))

    request.addfinalizer(fin)
    # Сохраняю ссылку на базовый url
    driver.url = url
    # Выдача драйвера из фикстуры
    return driver
