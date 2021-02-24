from page_objects.BasePage import BasePage


class CategoriesPage(BasePage):
    """Страница Categories"""

    MENU_CATALOG = {'css': '#menu-catalog'}
    MENU_CATEGORIES = {'css': '#collapse1 > li:nth-child(1) > a'}
    NAME_INPUT = {'css': '#input-name1'}
    TAG_TITLE_INPUT = {'css': '#input-meta-title1'}
    TABLE = {'css': '#form-category > div > table > tbody > tr'}
    VALUE = 'Apple_category_name 0'

    def open_categories(self):
        self._click(self.MENU_CATALOG)
        self._wait_for_visible(self.MENU_CATEGORIES)
        self._click(self.MENU_CATEGORIES)
        return self

    def input_data_categories(self, name_categories, tag_categories):
        self._wait_for_visible(self.NAME_INPUT)
        self._wait_to_be_clickable(self.NAME_INPUT)
        self._input(self.NAME_INPUT, name_categories)
        self._input(self.TAG_TITLE_INPUT, tag_categories)
        return self

    def find_table_categories(self):
        self._wait_for_visible(self.TABLE)

    def check_click(self):
        check_object = self._find_element_checkbox_in_table(self.TABLE, self.VALUE)
        self._click_checkbox_in_table(check_object)
