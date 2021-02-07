from lesson15.page_objects.AdminPage import AdminPage
from lesson15.page_objects.CategoriesPage import CategoriesPage
from lesson15.page_objects.ProductsPage import ProductsPage
from lesson15.page_objects.OptionsPage import OptionsPage
from lesson15.page_objects.ManufacturersPage import ManufacturersPage
import allure
import time


@allure.feature('OpenCart')
@allure.title('Login и logout страницы admin')
def test_admin_page_login_logout(browser):
    AdminPage(browser).go_to()
    AdminPage(browser).login_user()
    AdminPage(browser).logout_user()
    text_panel_title = AdminPage(browser).verify_logout()
    assert text_panel_title == 'Please enter your login details.'


@allure.feature('OpenCart')
@allure.title('Добавление новой categories')
def test_admin_page_add_categories(browser):
    AdminPage(browser).go_to()
    AdminPage(browser).login_user()
    CategoriesPage(browser).open_categories()
    AdminPage(browser).click_add_button()
    CategoriesPage(browser).input_data_categories('Apple_category_name', 'Apple_tag_title')
    AdminPage(browser).click_save_button()


@allure.feature('OpenCart')
@allure.title('Удаление categories')
def test_admin_page_delete_categories(browser):
    AdminPage(browser).go_to()
    AdminPage(browser).login_user()
    CategoriesPage(browser).open_categories()
    CategoriesPage(browser).find_table_categories()
    CategoriesPage(browser).check_click()
    AdminPage(browser).click_del_button()


@allure.feature('OpenCart')
@allure.title('Добавление нового products')
def test_admin_page_add_products(browser):
    AdminPage(browser).go_to()
    AdminPage(browser).login_user()
    ProductsPage(browser).open_products()
    AdminPage(browser).click_add_button()
    ProductsPage(browser).input_data_products('Apple_product_name', 'Apple_tag_title', 'Apple_model')
    AdminPage(browser).click_save_button()


@allure.feature('OpenCart')
@allure.title('Удаление products')
def test_admin_page_delete_products(browser):
    AdminPage(browser).go_to()
    AdminPage(browser).login_user()
    ProductsPage(browser).open_products()
    ProductsPage(browser).find_table_products()
    ProductsPage(browser).check_click()
    AdminPage(browser).click_del_button()


@allure.feature('OpenCart')
@allure.title('Добавление новой options')
def test_admin_page_add_options(browser):
    AdminPage(browser).go_to()
    AdminPage(browser).login_user()
    OptionsPage(browser).open_options()
    AdminPage(browser).click_add_button()
    OptionsPage(browser).input_data_option('Option_Name_date', 'Date', '123')
    AdminPage(browser).click_save_button()


@allure.feature('OpenCart')
@allure.title('Удаление options')
def test_admin_page_delete_options(browser):
    AdminPage(browser).go_to()
    AdminPage(browser).login_user()
    OptionsPage(browser).open_options()
    OptionsPage(browser).find_table_options()
    OptionsPage(browser).check_click()
    AdminPage(browser).click_del_button()


@allure.feature('OpenCart')
@allure.title('Добавление новой Manufacturers')
def test_admin_page_add_manufacturers(browser):
    AdminPage(browser).go_to()
    AdminPage(browser).login_user()
    ManufacturersPage(browser).open_manufacturers()
    AdminPage(browser).click_add_button()
    ManufacturersPage(browser).input_data_manufacturers('Manufacturers_Name')
    AdminPage(browser).click_save_button()


@allure.feature('OpenCart')
@allure.title('Удаление Manufacturers')
def test_admin_page_delete_manufacturers(browser):
    AdminPage(browser).go_to()
    AdminPage(browser).login_user()
    ManufacturersPage(browser).open_manufacturers()
    ManufacturersPage(browser).find_table_manufacturers()
    ManufacturersPage(browser).check_click()
    AdminPage(browser).click_del_button()