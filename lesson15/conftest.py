import pytest
from selenium.webdriver import ChromeOptions, FirefoxOptions, IeOptions
import logging
from selenium import webdriver

logging.basicConfig(level=logging.INFO, filename="logs\\selenium.log")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Please, choose your browser")
    # parser.addoption("--url", "-U", action="store", default="https://localhost/admin/")

    # parser.addoption("--bversion", action="store", required=True)
    parser.addoption("--vnc", action="store_true", default=False)
    parser.addoption("--logs", action="store_true", default=False)
    parser.addoption("--videos", action="store_true", default=False)
    parser.addoption("--executor", action="store", default="localhost")
    parser.addoption("--mobile", action="store_true")


# @pytest.fixture
# def url(request):
#     return request.config.getoption("--url")


@pytest.fixture
#def browser(request, url):
def browser(request):
    # Сбор параметров запуска для pytest
    browser = request.config.getoption("--browser")
    # version = request.config.getoption("--bversion")
    executor = request.config.getoption("--executor")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    videos = request.config.getoption("--videos")
    executor_url = f"http://{executor}:4444/wd/hub"
    mobile = request.config.getoption("--mobile")

    caps = {
        "browserName": browser,
        # "browserVersion": version,
        "screenResolution": "1280x720",
        "name": "Mikhail.C",
        "selenoid:options": {
            "enableVNC": vnc,
            "enableVideo": videos,
            "enableLog": logs,
        },
        'acceptSslCerts': True,
        'acceptInsecureCerts': True,
        'timeZone': 'Europe/Moscow',
        'goog:chromeOptions': {
            'args': []
        }
    }

    logger = logging.getLogger('BrowserLogger')
    test_name = request.node.name
    logger.info("===> Test {} started".format(test_name))

    """ Инициализация браузера """
    if browser == "chrome":
    # if browser == "chrome" and mobile:
    #     caps["goog:chromeOptions"]["mobileEmulation"] = {"deviceName": "iPhone 5/SE"}
        #  driver = webdriver.Chrome(executable_path=drivers + "/chromedriver")
        option = ChromeOptions()
        # option.add_argument('--disable-popup-blocking')
        option.add_argument('--ignore-certificate-errors')
        # option.add_argument('--headless')
        # driver = webdriver.Chrome(options=option)
        driver = webdriver.Remote(
            command_executor=executor_url,
            options=option,
            desired_capabilities=caps
        )
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
    #driver.url = url
    # Выдача драйвера из фикстуры
    return driver
