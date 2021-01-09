from .BasePage import BasePage
import time


class AdminPage(BasePage):
    """Страница администратора"""

    LOGIN_USER_NAME_INPUT = {'css': '#input-username'}
    LOGIN_PASSWORD_INPUT = {'css': '#input-password'}
    LOGIN_BUTTON = {"css": "button[type='submit']"}
    LOGOUT_BUTTON = {"css": "header > div > ul > li:nth-child(2) > a"}
    PANEL_TITLE = {"css": ".panel-title"}
    NAVIGATION_LIST = {"css": "#menu"}
    TABLE = {"css": "table > tbody > tr"}

    USER = 'user'
    PASSWORD = 'bitnami1'

    def login_user(self):
        self._input(self.LOGIN_USER_NAME_INPUT, self.USER)
        self._input(self.LOGIN_PASSWORD_INPUT, self.PASSWORD)
        self._click(self.LOGIN_BUTTON)
        return self

    def logout_user(self):
        self._click(self.LOGOUT_BUTTON)
        return self

    def verify_logout(self):
        return self._get_element_text(self.PANEL_TITLE)

    def verify_navigation_list(self):
        return self._get_element_text(self.NAVIGATION_LIST)