from lesson12.page_objects.BasePage import BasePage


class OptionsPage(BasePage):
    """Страница Options"""

    MENU_CATALOG = {'css': '#menu-catalog'}
    MENU_OPTIONS = {'css': '#collapse1 > li:nth-child(6)'}
    OPTION_NAME_INPUT = {'css': '#form-option > fieldset:nth-child(1) > div.form-group.required > div > div > input'}
    TYPE_SELECT_INPUT = {'css': '#input-type'}
    SORT_ORDER_INPUT = {'css': '#input-sort-order'}
    TABLE = {'css': '#form-option > div > table > tbody > tr'}
    VALUE = 'Option_Name_date 123'

    def open_options(self):
        self._click(self.MENU_CATALOG)
        self._wait_for_visible(self.MENU_OPTIONS)
        self._click(self.MENU_OPTIONS)
        return self

    def input_data_option(self, option_name, type_value, sort_order):
        self._wait_for_visible(self.OPTION_NAME_INPUT)
        self._input(self.OPTION_NAME_INPUT, option_name)
        self._select_by_value(self.TYPE_SELECT_INPUT, type_value)
        self._input(self.SORT_ORDER_INPUT, sort_order)
        return self

    def find_table_options(self):
        self._wait_for_visible(self.TABLE)

    def check_click(self):
        check_object = self._find_element_checkbox_in_table(self.TABLE, self.VALUE)
        self._click_checkbox_in_table(check_object)
