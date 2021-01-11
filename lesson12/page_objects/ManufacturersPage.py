from lesson12.page_objects.BasePage import BasePage


class ManufacturersPage(BasePage):
    """Страница Manufacturers"""

    MENU_CATALOG = {'css': '#menu-catalog'}
    MENU_MANUFACTURERS = {'css': '#collapse1 > li:nth-child(7)'}
    ADD_BUTTON = {'css': 'a.btn.btn-primary'}
    DEL_BUTTON = {'css': 'button[data-original-title=Delete]'}
    SAVE_BUTTON = {'css': 'div.pull-right > button.btn.btn-primary'}
    MANUFACTURERS_NAME_INPUT = {'css': '#input-name'}
    TABLE = {'css': '#form-manufacturer > div > table > tbody > tr'}
    VALUE = 'Manufacturers_Name 0'
    ALERT_SUCCESS = {'css': 'div.container-fluid > div.alert.alert-success.alert-dismissible'}

    def open_manufacturers(self):
        self._click(self.MENU_CATALOG)
        self._wait_for_visible(self.MENU_MANUFACTURERS)
        self._click(self.MENU_MANUFACTURERS)
        return self

    def click_add_button(self):
        self._wait_for_visible(self.ADD_BUTTON)
        self._click(self.ADD_BUTTON)
        return self

    def click_del_button(self):
        self._click(self.DEL_BUTTON)
        self._confirm_accept()
        self._wait_for_visible(self.ALERT_SUCCESS)
        return self

    def input_data_manufacturers(self, name_manufacturers):
        self._input(self.MANUFACTURERS_NAME_INPUT, name_manufacturers)
        return self

    def click_save_button(self):
        self._click(self.SAVE_BUTTON)
        return self

    def find_table_manufacturers(self):
        self._wait_for_visible(self.TABLE)

    def check_click(self):
        check_object = self._find_element_checkbox_in_table(self.TABLE, self.VALUE)
        self._click_checkbox_in_table(check_object)
