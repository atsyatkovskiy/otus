from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://localhost/admin/"

    # def _element(self, selector: dict, link_text: str = None):
    #     by = None
    #     if link_text:
    #         by = By.LINK_TEXT
    #     elif 'css' in selector.keys():
    #         by = By.CSS_SELECTOR
    #         selector = selector['css']
    #     elif 'xpath':
    #         by = By.XPATH
    #     return self.driver.find_element(by, selector)

    def _element(self, selector: dict, index=0, link_text: str = None):
        by = None
        if link_text:
            by = By.LINK_TEXT
        elif 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
        elif 'xpath':
            by = By.XPATH
        return self.driver.find_elements(by, selector)[index]

    def _elements(self, selector: dict, link_text: str = None):
        by = None
        if link_text:
            by = By.LINK_TEXT
        elif 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
        return self.driver.find_elements(by, selector)

    def _find_element_checkbox_in_table(self, selector: dict, value_text: str):
        by = By.CSS_SELECTOR
        selector_css = selector['css']
        a = self.driver.find_elements(by, selector_css)
        for i in a:
            if i.text == value_text:
                print(f"Элемент найден, это:", i.text)
                return i.find_element(by, 'input[type=checkbox]')
            else:
                print(f"Элемент не найден, это:", i.text)

    # def _find_element_checkbox_in_table(self, selector: dict, value_text: str):
    #     for css in selector.keys():
    #         print('вошли в первый цикл!!!!')
    #         by = By.CSS_SELECTOR
    #         selector_css = selector['css']
    #         a = self.driver.find_elements(by, selector_css)
    #         for i in a:
    #             if i.text == value_text:
    #                 print(f"Элемент найден, это:", i.text)
    #                 return i.find_element(by, 'input[type=checkbox]')
    #             else:
    #                 print(f"Элемент не найден, это:", i.text)

    def _click_checkbox_in_table(self, element_object):
        element_object.click()

    def _confirm_accept(self):
        confirm = self.driver.switch_to.alert
        confirm.accept()

    def _click(self, selector, index=0):
        ActionChains(self.driver).move_to_element(self._element(selector, index)).click().perform()

    def _input(self, selector, value):
        element = self._element(selector)
        element.clear()
        element.send_keys(value)

    # def _wait_for_visible(self, selector, link_text=None, wait=5):
    #     return WebDriverWait(self.driver, wait).until(EC.visibility_of(self._element(selector, link_text)))

    def _wait_for_visible(self, selector, link_text=None, index=0, wait=5):
        return WebDriverWait(self.driver, wait).until(EC.visibility_of(self._element(selector, index, link_text)))

    def _wait_to_be_clickable(self, selector, link_text=None, index=0, wait=5):
        return WebDriverWait(self.driver, wait).until(EC.element_to_be_clickable(self._element(selector, index, link_text)))

    def _presence_of_element_located(self, selector, link_text=None, wait=5):
        return WebDriverWait(self.driver, wait).until(EC.presence_of_element_located(self._element(selector, link_text)))

    def _get_element_text(self, selector):
        return self._element(selector).text

    def go_to(self):
        return self.driver.get(self.base_url)

