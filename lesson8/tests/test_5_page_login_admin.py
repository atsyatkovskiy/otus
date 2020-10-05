import time
from selenium.webdriver.common.by import By


# Проверка title загруженной страницы
# localhost/index.php?route=account/login
def test_account_login_page_title(browser):
    browser.get(browser.url + "/index.php?route=account/login")
    assert "Account Login" in browser.title


# Проверка "New Customer", и button Сontinue
# localhost/index.php?route=account/login
def test_account_login_page_new_customer(browser):
    browser.get(browser.url + "/index.php?route=account/login")
    new_customer = browser.find_element_by_css_selector("#content > div > div:nth-child(1) > div > h2")
    assert "New Customer" == new_customer.text
    button_continue = browser.find_element_by_css_selector("#content > div > div:nth-child(1) > div > a")
    button_continue.click()


# Проверка "Returning Customer", button Login
# localhost/index.php?route=account/login
def test_account_login_page_returning_customer(browser):
    browser.get(browser.url + "/index.php?route=account/login")
    returning_customer = browser.find_element_by_css_selector("#content > div > div:nth-child(2) > div > h2")
    assert "Returning Customer" == returning_customer.text
    button_login = browser.find_element_by_css_selector("#content > div > div:nth-child(2) > div > form > input")
    button_login.click()


# Проверка "input" e-mail и password
# localhost/index.php?route=account/login
def test_account_login_page_input(browser):
    browser.get(browser.url + "/index.php?route=account/login")
    input_email = browser.find_element_by_css_selector("#input-email")
    input_email.send_keys("qweasdzxc@ya.ru")
    input_password = browser.find_element_by_css_selector("#input-password")
    input_password.send_keys("123456789")
    button_login = browser.find_element_by_css_selector("#content > div > div:nth-child(2) > div > form > input")
    button_login.click()


# Проверка list Group
# localhost/index.php?route=account/login
def test_account_login_page_list_group(browser):
    browser.get(browser.url + "/index.php?route=account/login")
    list_group_element = browser.find_element_by_css_selector("#column-right > div")
    for i in range(0, 13):
        i += 1
        text_item = list_group_element.find_element_by_css_selector(f'#column-right > div > a:nth-child({i})').text
        assert list_group[i - 1] == text_item


list_group = ["Login",
              "Register",
              "Forgotten Password",
              "My Account",
              "Address Book",
              "Wish List",
              "Order History",
              "Downloads",
              "Recurring payments",
              "Reward Points",
              "Returns",
              "Transactions",
              "Newsletter"]
