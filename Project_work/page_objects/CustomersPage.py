from page_objects.BasePage import BasePage


class CustomersPage(BasePage):
    """Страница Categories"""

    MENU_CUSTOMERS = {'css': '#menu-customer > a'}
    MENU_CUSTOMERS_CHILD = {'css': '#collapse5 > li:nth-child(1) > a'}
    # #form-customer > table > tbody > tr
    # NAME_INPUT = {'css': '#input-name1'}
    # TAG_TITLE_INPUT = {'css': '#input-meta-title1'}
    TABLE = {'css': '#form-customer > table > tbody > tr'}
    VALUE = 'Name Last_name 123@123.com Default Enabled 172.18.0.1 26/02/2021'

    def open_customers(self):
        self._click(self.MENU_CUSTOMERS)
        self._wait_for_visible(self.MENU_CUSTOMERS_CHILD)
        self._click(self.MENU_CUSTOMERS_CHILD)
        return self

    def find_table_customers(self):
        self._wait_for_visible(self.TABLE)

    def check_click(self):
        check_object = self._find_element_checkbox_in_table(self.TABLE, self.VALUE)
        self._click_checkbox_in_table(check_object)
