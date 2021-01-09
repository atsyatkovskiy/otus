import pytest
from selenium.webdriver import ChromeOptions, FirefoxOptions, IeOptions
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


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
    request.addfinalizer(driver.quit)
    # Сохраняю ссылку на базовый url
    driver.url = url
    # Выдача драйвера из фикстуры
    return driver


@pytest.fixture
def wait(browser):
    wait = WebDriverWait(browser, 10)
    yield wait

# def highlight(browser):
#     element = browser.find_element(By.CSS_SELECTOR, "#input-sort")
#     """Highlights (blinks) a Selenium Webdriver element"""
#     browser = element._parent
#     def apply_style(s):
#         browser.execute_script("arguments[0].setAttribute('style', arguments[1]);",
#                               element, s)
#     original_style = element.get_attribute('style')
#     apply_style("background: yellow; border: 2px solid red;")
#     time.sleep(3)
#     apply_style(original_style)
