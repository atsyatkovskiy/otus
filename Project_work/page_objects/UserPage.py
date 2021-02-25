from page_objects.BasePage import BasePage
import allure
import time


class UserPage(BasePage):
    """Страница user home"""
    MY_ACCOUNT = {"css": "#top-links > ul > li.dropdown > a > span.hidden-xs.hidden-sm.hidden-md"}
    REGISTER_LINK = {"css": "#top-links > ul > li.dropdown.open > ul > li:nth-child(1) > a"}
    LOGIN_LINK = {"css": "#top-links > ul > li.dropdown.open > ul > li:nth-child(2) > a"}
    LOGOUT_LINK = {"css": "#top-links > ul > li.dropdown.open > ul > li:nth-child(5) > a"}

    PANEL_TITLE_REGISTER_ACCOUNT = {"css": "#content > h1"}

    FIRST_NAME_INPUT = {'css': '#input-firstname'}
    LAST_NAME_INPUT = {'css': '#input-lastname'}
    EMAIL_INPUT = {'css': '#input-email'}
    TELEPHONE_INPUT = {'css': '#input-telephone'}
    PASSWORD_INPUT = {'css': '#input-password'}
    ADDRESS1_INPUT = {'css': '#input-address-1'}
    CITY_INPUT = {'css': '#input-city'}

    COUNTRY_SELECT_INPUT = {'css': '#input-country'}
    REGION_SELECT_INPUT = {'css': '#input-zone'}
    DEFAULT_ADDRESS_RADIO_BUTTON = {'css': 'input[type=radio][value=1]'}
    PASSWORD_CONFIRM_INPUT = {'css': '#input-confirm'}
    ADDRESS_BOOK_ITEM_MENU = {'css': '#column-right > div > a:nth-child(4)'}
    NEW_ADDRESS_BUTTON = {'css': '#content > div > div.pull-right > a'}

    AGREE_CHECK = {"css": "input[type=checkbox]"}

    CONTINUE_BUTTON = {"css": "#content > form > div > div > input.btn.btn-primary"}
    PANEL_TITLE_HAS_BEEN_CREATED = {"css": "#content > h1"}
    RETURNING_CUSTOMER_HEADER = {"css": "#content > div > div:nth-child(2) > div > h2"}
    ACCOUNT_LOGOUT_HEADER = {"css": "#content > h1"}

    LOGIN_BUTTON = {"css": "#content > div > div:nth-child(2) > div > form > input"}

    NAVIGATION_LIST_MENU_USER = {"css": "#column-right > div"}
    ALERT_EMAIL_ALREADY_REGISTERED = {'css': '#account-register > div.alert.alert-danger.alert-dismissible'}
    ALERT_SUCCESS_ADDED = {"css": "#account-address > div.alert.alert-success.alert-dismissible"}

    URL = "http://192.168.1.34/"

    def input_user_data(self, first_name, last_name, email, telephone, password, password_conf):
        self._input(self.FIRST_NAME_INPUT, first_name)
        self._input(self.LAST_NAME_INPUT, last_name)
        self._input(self.EMAIL_INPUT, email)
        self._input(self.TELEPHONE_INPUT, telephone)
        self._input(self.PASSWORD_INPUT, password)
        self._input(self.PASSWORD_CONFIRM_INPUT, password_conf)
        return self

    def input_add_address(self, first_name, last_name, address1, city, country, region):
        self._input(self.FIRST_NAME_INPUT, first_name)
        self._input(self.LAST_NAME_INPUT, last_name)
        self._input(self.ADDRESS1_INPUT, address1)
        self._input(self.CITY_INPUT, city)
        self._select_by_value(self.COUNTRY_SELECT_INPUT, country)
        self._select_by_value(self.REGION_SELECT_INPUT, region)
        #  self._radio_button_value(self.DEFAULT_ADDRESS_RADIO_BUTTON)
        self._click(self.CONTINUE_BUTTON)
        return self

    def input_login_email_password(self, email, password):
        self._input(self.EMAIL_INPUT, email)
        self._input(self.PASSWORD_INPUT, password)
        self._click(self.LOGIN_BUTTON)
        return self

    def verify_register_page(self):
        return self._get_element_text(self.PANEL_TITLE_REGISTER_ACCOUNT)

    def verify_has_been_created_page(self):
        return self._get_element_text(self.PANEL_TITLE_HAS_BEEN_CREATED)

    def verify_returning_customer(self):
        return self._get_element_text(self.RETURNING_CUSTOMER_HEADER)

    def verify_list_menu_user(self):
        self._wait_for_visible(self.NAVIGATION_LIST_MENU_USER)
        return self._get_element_text(self.NAVIGATION_LIST_MENU_USER)

    def verify_account_logout(self):
        return self._get_element_text(self.ACCOUNT_LOGOUT_HEADER)

    def verify_alert(self):
        return self._get_element_text(self.ALERT_EMAIL_ALREADY_REGISTERED)

    def verify_alert_successfully_added(self):
        return self._get_element_text(self.ALERT_SUCCESS_ADDED)

    def click_continue_button(self):
        self._click(self.CONTINUE_BUTTON)
        return self

    def click_check_agree(self):
        self._click(self.AGREE_CHECK)
        return self

    def click_my_account(self):
        self._click(self.MY_ACCOUNT)
        return self

    def click_my_account_register(self):
        self._click(self.REGISTER_LINK)
        return self

    def click_my_account_login(self):
        self._click(self.LOGIN_LINK)
        return self

    def click_my_account_logout(self):
        # self._presence_of_element_located(self.LOGOUT_LINK)
        self._click(self.LOGOUT_LINK)
        return self

    def click_address_book_new_address(self):
        self._click(self.ADDRESS_BOOK_ITEM_MENU)
        self._click(self.NEW_ADDRESS_BUTTON)
        return self

    def go_to(self):
        self._go_to(self.URL)
        return self
