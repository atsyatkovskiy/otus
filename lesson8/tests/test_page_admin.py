import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytesseract
from PIL import Image


# Login
# localhost/admin/
@pytest.fixture
def login(browser):
    """
    1) Вводим login, password и жмем на кнопку login
    """
    browser.get(browser.url + "/admin/")
    input_login = browser.find_element(By.CSS_SELECTOR, "#input-username")
    input_login.send_keys("user")
    input_password = browser.find_element(By.CSS_SELECTOR, "#input-password")
    input_password.send_keys("bitnami1")
    submit = browser.find_element_by_css_selector("button[type='submit']")
    submit.click()


# Проверка Logout
# localhost/admin/
def test_admin_page_login_logout(browser, wait, login):
    """
    1) Поиск имени юзера John Doe
    """
    icon_profile = browser.find_element(By.CSS_SELECTOR, ".dropdown")
    icon_profile.get_attribute("class")
    assert "John Doe" == icon_profile.text
    """
    2) Жмем на Logout
    """
    link_logout = browser.find_element(By.CSS_SELECTOR, "header > div > ul > li:nth-child(2) > a")
    link_logout.click()
    """
    3) Ищем и жмем на Login
    """
    browser.find_element_by_css_selector("button[type='submit']").click()
    """
    4) Проверяем текст panel_heading
    """
    text_panel_heading = browser.find_element(By.CSS_SELECTOR, ".panel-title").text
    assert text_panel_heading == "Please enter your login details."


# Создаем новую категорию
# localhost/admin/
def test_admin_page_add_categories(browser, wait, login):
    """
    1) Клик Catalog -> Categories и переход на страницу Categories
    """
    browser.find_element(By.CSS_SELECTOR, "#menu-catalog").click()
    el_cat = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#collapse1 > li:nth-child(1) > a")))
    assert el_cat.get_property("innerText") == "Categories"
    el_cat.click()
    """
    2) На странице Catalog жмём на кнопку "Add new"
    """
    page_header = browser.find_element(By.CSS_SELECTOR, "#content > div.page-header > div > h1")
    assert page_header.text == "Categories"
    button_add_new = browser.find_element(By.CSS_SELECTOR, "a.btn.btn-primary")
    button_add_new.click()
    """
    3) На странице Catalog, раздел Add Category заполняем поля:
    Category Name: Apple_category_name
    Meta Tag Title: Apple_tag_title
    """
    input_name_categories = browser.find_element(By.CSS_SELECTOR, "#input-name1")
    input_name_categories.send_keys("Apple_category_name")
    input_tag_title = browser.find_element(By.CSS_SELECTOR, "#input-meta-title1")
    input_tag_title.send_keys("Apple_tag_title")
    """
    4) Жмем на кнопку Save и проверяем, появился ли alert_success:
    """
    button_save = browser.find_element(By.CSS_SELECTOR, "div.pull-right > button.btn.btn-primary")
    button_save.click()
    alert_success = browser.find_element(By.CSS_SELECTOR, "div.alert.alert-success.alert-dismissible").text
    assert alert_success == "Success: You have modified categories!\n×"


# Удаляем ранее созданную категорию Apple_category_name
# localhost/admin/
def test_admin_page_delete_categories(browser, wait, login):
    """
    1) Клик Catalog -> Categories и переход на страницу Categories
    """
    browser.find_element(By.CSS_SELECTOR, "#menu-catalog").click()
    el_cat = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#collapse1 > li:nth-child(1) > a")))
    assert el_cat.get_property("innerText") == "Categories"
    el_cat.click()

    """
    2) Проверяем, есть ли в таблице новая категория Apple_category_name
    """
    for i in range(0, 20):
        i += 1
        text_tr = browser.find_element(By.CSS_SELECTOR, f'table > tbody > tr:nth-child({i})').text
        if text_tr == "Apple_category_name 0":
            check = browser.find_element(By.CSS_SELECTOR,
                                         f'table > tbody > tr:nth-child({i}) > td.text-center > input[type=checkbox]')
            check.click()
            break
        else:
            print(f"Элемент {text_tr} не найден")
    """
    3) Жмем на кнопку удалить
    """
    button_del = browser.find_element(By.CSS_SELECTOR, "#content > div.page-header > div > div > button")
    button_del.click()
    """
    4) В alert жмем на кнопку OK и проверяем, появился ли alert_success
    """
    # browser.execute_script("alert('test_alert')")  /вызов алерта в браузере
    confirm = browser.switch_to.alert
    # print(confirm.text)
    confirm.accept()
    alert_success = browser.find_element(By.CSS_SELECTOR, "div.alert.alert-success.alert-dismissible").text
    assert alert_success == "Success: You have modified categories!\n×"


