import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir = os.path.dirname(parentdir)
sys.path.insert(0, parentdir)

from page_objects.AdminPage import AdminPage
from page_objects.UserPage import UserPage
from page_objects.CustomersPage import CustomersPage
import allure
import time


@allure.feature('OpenCart customer')
@allure.story('Регистрация customer')
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
    # text_has_been_created = UserPage(browser).verify_register_page()
    # assert text_has_been_created == 'Your Account Has Been Created!'


@allure.feature('OpenCart customer')
@allure.story('Сustomer существует')
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


@allure.feature('OpenCart customer')
@allure.story('Логин и разлогин customer')
@allure.title('Логин и разлогин юзера')
def test_login_logout(browser):
    UserPage(browser).go_to()
    UserPage(browser).click_my_account()
    UserPage(browser).click_my_account_login()
    text_returning_customer = UserPage(browser).verify_returning_customer()
    assert text_returning_customer == 'Returning Customer'
    UserPage(browser).input_login_email_password('123@123.com', '1234')
    # text_list_menu_user = UserPage(browser).verify_list_menu_user()
    # assert text_list_menu_user == str_menu_user
    UserPage(browser).click_my_account()
    UserPage(browser).click_my_account_logout()
    text_account_logout = UserPage(browser).verify_account_logout()
    assert text_account_logout == 'Account Logout'


@allure.feature('OpenCart customer')
@allure.story('Адрес customer')
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


@allure.feature('OpenCart customer')
@allure.story('Удаление customer')
@allure.title('Удаление покупателя из БД магазина')
def test_admin_page_delete_customers(browser):
    AdminPage(browser).go_to()
    AdminPage(browser).login_user()
    CustomersPage(browser).open_customers()
    CustomersPage(browser).find_table_customers()
    CustomersPage(browser).check_click()
    AdminPage(browser).click_del_button()


# str_menu_user = 'My Account\nEdit Account\nPassword\nAddress Book\nWish List\nOrder History\nDownloads\nRecurring ' \
#                'payments\nReward Points\nReturns\nTransactions\nNewsletter\nLogout'

