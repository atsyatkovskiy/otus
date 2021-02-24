from page_objects.BasePage import BasePage
import allure
import time


class AdminPage(BasePage):
    """Страница администратора"""

    LOGIN_USER_NAME_INPUT = {'css': '#input-username'}
    LOGIN_PASSWORD_INPUT = {'css': '#input-password'}
    LOGIN_BUTTON = {"css": "button[type='submit']"}
    LOGOUT_BUTTON = {"css": ".nav > li:nth-child(2)"}
    PANEL_TITLE = {"css": ".panel-title"}
    NAVIGATION_LIST = {"css": "#menu"}
    ADD_BUTTON = {'css': 'a.btn.btn-primary'}
    DEL_BUTTON = {'css': 'button[data-original-title=Delete]'}
    SAVE_BUTTON = {'css': 'div.pull-right > button.btn.btn-primary'}
    ALERT_SUCCESS = {'css': 'div.container-fluid > div.alert.alert-success.alert-dismissible'}

    USER = 'user'
    PASSWORD = 'bitnami'
    URL = "http://192.168.1.34/admin/"
    # URL = "http://demo.opencart.com/admin"

    def login_user(self):
        self._input(self.LOGIN_USER_NAME_INPUT, self.USER)
        self._input(self.LOGIN_PASSWORD_INPUT, self.PASSWORD)
        self._click(self.LOGIN_BUTTON)
        return self

    def logout_user(self):
        self._wait_for_visible(self.LOGOUT_BUTTON)
        self._click(self.LOGOUT_BUTTON)
        return self

    def verify_logout(self):
        return self._get_element_text(self.PANEL_TITLE)

    def verify_navigation_list(self):
        return self._get_element_text(self.NAVIGATION_LIST)

    def click_add_button(self):
        self._wait_for_visible(self.ADD_BUTTON)
        self._click(self.ADD_BUTTON)
        return self

    def click_del_button(self):
        self._click(self.DEL_BUTTON)
        self._confirm_accept()
        self._wait_for_visible(self.ALERT_SUCCESS)
        return self

    def click_save_button(self):
        self._click(self.SAVE_BUTTON)
        return self

    def go_to(self):
        self._go_to(self.URL)
        return self
