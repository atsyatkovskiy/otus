from page_objects.BasePage import BasePage


class ManufacturersPage(BasePage):
    """Страница Manufacturers"""

    MENU_CATALOG = {'css': '#menu-catalog'}
    MENU_MANUFACTURERS = {'css': '#collapse1 > li:nth-child(7)'}
    MANUFACTURERS_NAME_INPUT = {'css': '#input-name'}
    TABLE = {'css': '#form-manufacturer > div > table > tbody > tr'}
    VALUE = 'Manufacturers_Name 0'

    def open_manufacturers(self):
        self._click(self.MENU_CATALOG)
        self._wait_for_visible(self.MENU_MANUFACTURERS)
        self._click(self.MENU_MANUFACTURERS)
        return self

    def input_data_manufacturers(self, name_manufacturers):
        self._input(self.MANUFACTURERS_NAME_INPUT, name_manufacturers)
        return self

    def find_table_manufacturers(self):
        self._wait_for_visible(self.TABLE)

    def check_click(self):
        check_object = self._find_element_checkbox_in_table(self.TABLE, self.VALUE)
        self._click_checkbox_in_table(check_object)
