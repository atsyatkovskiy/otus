from lesson12.page_objects.BasePage import BasePage


class ProductsPage(BasePage):
    """Страница Products"""

    MENU_CATALOG = {'css': '#menu-catalog'}
    MENU_PRODUCTS = {'css': '#collapse1 > li:nth-child(2) > a'}
    NAME_INPUT = {'css': '#input-name1'}
    TAG_TITLE_INPUT = {'css': '#input-meta-title1'}
    MODEL_INPUT = {'css': '#input-model'}
    DATA_BUTTON = {'css': '#form-product > ul > li:nth-child(2) > a'}
    TABLE = {'css': '#form-product > div > table > tbody > tr'}
    VALUE = 'Apple_product_name Apple_model $0.00 1 Enabled'

    def open_products(self):
        self._wait_for_visible(self.MENU_CATALOG)
        self._click(self.MENU_CATALOG)
        self._wait_for_visible(self.MENU_PRODUCTS)
        self._click(self.MENU_PRODUCTS)
        return self

    def input_data_products(self, name_products, tag_products, model):
        self._wait_for_visible(self.NAME_INPUT)
        self._input(self.NAME_INPUT, name_products)
        self._wait_for_visible(self.TAG_TITLE_INPUT)
        self._input(self.TAG_TITLE_INPUT, tag_products)
        self._click(self.DATA_BUTTON)
        self._wait_for_visible(self.MODEL_INPUT)
        self._input(self.MODEL_INPUT, model)
        return self

    def find_table_products(self):
        self._wait_for_visible(self.TABLE)

    def check_click(self):
        check_object = self._find_element_checkbox_in_table(self.TABLE, self.VALUE)
        self._click_checkbox_in_table(check_object)
