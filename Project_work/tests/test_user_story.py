import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0, parentdir)

from page_objects.AdminPage import AdminPage
from page_objects.UserPage import UserPage
import allure
import time


@allure.feature('OpenCart User')
@allure.title('Регистрация нового юзера')
def test_user_registration(browser):
    UserPage(browser).go_to()
    UserPage(browser).click_my_account()
    UserPage(browser).click_my_account_register()
    text_register_page = UserPage(browser).verify_register_page()
    assert text_register_page == 'Register Account'
    UserPage(browser).input_user_data('Name', 'Last_name', '123@123.com', '+1234567', '1234', '1234')
    UserPage(browser).click_check_agree()
    UserPage(browser).click_continue_button()
    text_has_been_created = UserPage(browser).verify_register_page()
    assert text_has_been_created == 'Your Account Has Been Created!'


@allure.feature('OpenCart User')
@allure.title('Тест, что юзер с такими e-mail уже существует')
def test_user_failed_registration(browser):
    UserPage(browser).go_to()
    UserPage(browser).click_my_account()
    UserPage(browser).click_my_account_register()
    text_register_page = UserPage(browser).verify_register_page()
    assert text_register_page == 'Register Account'
    UserPage(browser).input_user_data('Name', 'Last_name', '123@123.com', '+1234567', '1234', '1234')
    UserPage(browser).click_check_agree()
    UserPage(browser).click_continue_button()
    text_address_is_already_registered = UserPage(browser).verify_alert()
    assert text_address_is_already_registered == 'Warning: E-Mail Address is already registered!'


@allure.feature('OpenCart User')
@allure.title('Логин и разлогин юзера')
def test_login_logout(browser):
    UserPage(browser).go_to()
    UserPage(browser).click_my_account()
    UserPage(browser).click_my_account_login()
    text_returning_customer = UserPage(browser).verify_returning_customer()
    assert text_returning_customer == 'Returning Customer'
    UserPage(browser).input_login_email_password('123@123.com', '1234')
    text_list_menu_user = UserPage(browser).verify_list_menu_user()
    assert text_list_menu_user == str_menu_user
    UserPage(browser).click_my_account()
    UserPage(browser).click_my_account_logout()
    text_account_logout = UserPage(browser).verify_account_logout()
    assert text_account_logout == 'Account Logout'


@allure.feature('OpenCart User')
@allure.title('Добавляем новый адрес юзера')
def test_new_address(browser):
    UserPage(browser).go_to()
    UserPage(browser).click_my_account()
    UserPage(browser).click_my_account_login()
    text_returning_customer = UserPage(browser).verify_returning_customer()
    assert text_returning_customer == 'Returning Customer'
    UserPage(browser).input_login_email_password('123@123.com', '1234')
    UserPage(browser).click_address_book_new_address()
    UserPage(browser).input_add_address('Name', 'Last_name', 'Address1', 'City', 'Russian Federation', 'Moscow')
    text_successfully_added = UserPage(browser).verify_alert_successfully_added()
    assert text_successfully_added == 'Your address has been successfully added'


# @allure.feature('OpenCart')
# @allure.title('Удаление categories - Apple_category_name')
# def test_admin_page_delete_categories(browser):
#     AdminPage(browser).go_to()
#     AdminPage(browser).login_user()
#     CategoriesPage(browser).open_categories()
#     CategoriesPage(browser).find_table_categories()
#     CategoriesPage(browser).check_click()
#     AdminPage(browser).click_del_button()
#
#
# @allure.feature('OpenCart')
# @allure.title('Добавление нового products')
# def test_admin_page_add_products(browser):
#     AdminPage(browser).go_to()
#     AdminPage(browser).login_user()
#     ProductsPage(browser).open_products()
#     AdminPage(browser).click_add_button()
#     ProductsPage(browser).input_data_products('Apple_product_name', 'Apple_tag_title', 'Apple_model')
#     AdminPage(browser).click_save_button()
#
#
# @allure.feature('OpenCart')
# @allure.title('Удаление products - Apple_product_name')
# def test_admin_page_delete_products(browser):
#     AdminPage(browser).go_to()
#     AdminPage(browser).login_user()
#     ProductsPage(browser).open_products()
#     ProductsPage(browser).find_table_products()
#     ProductsPage(browser).check_click()
#     AdminPage(browser).click_del_button()
#
#
# @allure.feature('OpenCart')
# @allure.title('Добавление новой options')
# def test_admin_page_add_options(browser):
#     AdminPage(browser).go_to()
#     AdminPage(browser).login_user()
#     OptionsPage(browser).open_options()
#     AdminPage(browser).click_add_button()
#     OptionsPage(browser).input_data_option('Option_Name_date', 'Date', '123')
#     AdminPage(browser).click_save_button()
#
#
# @allure.feature('OpenCart')
# @allure.title('Удаление options - Option_Name_date')
# def test_admin_page_delete_options(browser):
#     AdminPage(browser).go_to()
#     AdminPage(browser).login_user()
#     OptionsPage(browser).open_options()
#     OptionsPage(browser).find_table_options()
#     OptionsPage(browser).check_click()
#     AdminPage(browser).click_del_button()
#
#
# @allure.feature('OpenCart')
# @allure.title('Добавление новой Manufacturers')
# def test_admin_page_add_manufacturers(browser):
#     AdminPage(browser).go_to()
#     AdminPage(browser).login_user()
#     ManufacturersPage(browser).open_manufacturers()
#     AdminPage(browser).click_add_button()
#     ManufacturersPage(browser).input_data_manufacturers('Manufacturers_Name')
#     AdminPage(browser).click_save_button()
#
#
# @allure.feature('OpenCart')
# @allure.title('Удаление Manufacturers - Manufacturers_Name')
# def test_admin_page_delete_manufacturers(browser):
#     AdminPage(browser).go_to()
#     AdminPage(browser).login_user()
#     ManufacturersPage(browser).open_manufacturers()
#     ManufacturersPage(browser).find_table_manufacturers()
#     ManufacturersPage(browser).check_click()
#     AdminPage(browser).click_del_button()

str_menu_user = 'My Account\nEdit Account\nPassword\nAddress Book\nWish List\nOrder History\nDownloads\nRecurring ' \
                'payments\nReward Points\nReturns\nTransactions\nNewsletter\nLogout'

