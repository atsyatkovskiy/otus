from lesson12.page_objects.AdminPage import AdminPage
from lesson12.page_objects.CategoriesPage import CategoriesPage
from lesson12.page_objects.ProductsPage import ProductsPage
import time


def test_admin_page_login_logout(browser):
    AdminPage(browser).go_to()
    AdminPage(browser).login_user()
    # navigation_list = AdminPage(browser).verify_navigation_list()
    # list_nav_correct = ['Dashboard',
    #                     'Catalog',
    #                     'Extensions',
    #                     'Design',
    #                     'Sales',
    #                     'Customers',
    #                     'Marketing',
    #                     'System',
    #                     'Reports']
    # for word in navigation_list.split():
    #     navigation_list.append(word)
    # assert navigation_list == list_nav_correct
    AdminPage(browser).logout_user()
    text_panel_title = AdminPage(browser).verify_logout()
    assert text_panel_title == 'Please enter your login details.'


def test_admin_page_add_categories(browser):
    AdminPage(browser).go_to()
    AdminPage(browser).login_user()
    CategoriesPage(browser).open_categories()
    CategoriesPage(browser).click_add_button()
    CategoriesPage(browser).input_data_categories('Apple_category_name', 'Apple_tag_title')
    CategoriesPage(browser).click_save_button()


def test_admin_page_delete_categories(browser):
    AdminPage(browser).go_to()
    AdminPage(browser).login_user()
    CategoriesPage(browser).open_categories()
    CategoriesPage(browser).find_table_categories()
    CategoriesPage(browser).check_click()
    CategoriesPage(browser).click_del_button()


def test_admin_page_add_products(browser):
    AdminPage(browser).go_to()
    AdminPage(browser).login_user()
    ProductsPage(browser).open_products()
    ProductsPage(browser).click_add_button()
    ProductsPage(browser).input_data_products('Apple_product_name', 'Apple_tag_title', 'Apple_model')
    ProductsPage(browser).click_save_button()


def test_admin_page_delete_products(browser):
    AdminPage(browser).go_to()
    AdminPage(browser).login_user()
    ProductsPage(browser).open_products()
    ProductsPage(browser).find_table_products()
    ProductsPage(browser).check_click()
    # time.sleep(3)
    ProductsPage(browser).click_del_button()

