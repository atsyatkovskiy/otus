from lesson12.page_objects.BasePage import BasePage


class CategoriesPage(BasePage):
    """Страница Categories"""

    MENU_CATALOG = {'css': '#menu-catalog'}
    MENU_CATEGORIES = {'css': '#collapse1 > li:nth-child(1) > a'}
    ADD_BUTTON = {'css': 'a.btn.btn-primary'}
    DEL_BUTTON = {'css': 'button[data-original-title=Delete]'}
    SAVE_BUTTON = {'css': 'div.pull-right > button.btn.btn-primary'}
    NAME_INPUT = {'css': '#input-name1'}
    TAG_TITLE_INPUT = {'css': '#input-meta-title1'}
    TABLE = {'css': '#form-category > div > table > tbody > tr'}
    VALUE = 'Apple_category_name 0'
    ALERT_SUCCESS = {'css': 'div.container-fluid > div.alert.alert-success.alert-dismissible'}

    def open_categories(self):
        self._click(self.MENU_CATALOG)
        self._click(self.MENU_CATEGORIES)
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

    def input_data_categories(self, name_categories, tag_categories):
        self._input(self.NAME_INPUT, name_categories)
        self._input(self.TAG_TITLE_INPUT, tag_categories)
        return self

    def click_save_button(self):
        self._click(self.SAVE_BUTTON)
        return self

    def find_table_categories(self):
        self._wait_for_visible(self.TABLE)

    def check_click(self):
        check_object = self._find_element_checkbox_in_table(self.TABLE, self.VALUE)
        self._click_checkbox_in_table(check_object)
