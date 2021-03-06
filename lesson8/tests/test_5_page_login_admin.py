import time
from selenium.webdriver.common.by import By


# Проверка title загруженной страницы
# localhost/admin/
def test_admin_page_title(browser):
    browser.get(browser.url + "/admin/")
    assert "Administration" in browser.title


# Проверка heading загруженной страницы
# localhost/admin/
def test_admin_page_heading(browser):
    browser.get(browser.url + "/admin/")
    heading = browser.find_element(By.CSS_SELECTOR, ".panel-title")
    assert "Please enter your login details." == heading.text


# Проверка заполнения input login, input password и submit
# localhost/admin/
def test_admin_page_input_login_pass(browser):
    browser.get(browser.url + "/admin/")
    input_login = browser.find_element(By.CSS_SELECTOR, "#input-username")
    input_login.send_keys("user")
    input_password = browser.find_element(By.CSS_SELECTOR, "#input-password")
    input_password.send_keys("bitnami1")
    submit = browser.find_element_by_css_selector("button[type='submit']")
    submit.click()


# Проверка ссылки Forgotten Password
# localhost/admin/
def test_admin_page_forgotten_password(browser):
    browser.get(browser.url + "/admin/")
    text_link = browser.find_element_by_link_text("Forgotten Password")
    text_link.click()


# Проверка текс label (Username, password)
# localhost/admin/
def test_admin_page_label(browser):
    browser.get(browser.url + "/admin/")
    label_username = browser.find_element(By.CSS_SELECTOR, "form > div:nth-child(1) > label")
    placeholder_username = browser.find_element(By.CSS_SELECTOR, "#input-username").get_attribute("placeholder")
    assert label_username.text == 'Username'
    assert placeholder_username == 'Username'

    label_password = browser.find_element_by_css_selector("form > div:nth-child(2) > label")
    placeholder_password = browser.find_element(By.CSS_SELECTOR, "#input-password").get_attribute("placeholder")
    assert label_password.text == 'Password'
    assert placeholder_password == 'Password'
    # time.sleep(5)
