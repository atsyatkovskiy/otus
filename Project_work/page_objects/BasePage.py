from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import allure
import logging


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        # self.base_url = "https://localhost/admin/"
        self.logger = logging.getLogger(type(self).__name__)

    @allure.step("Поиск элемента: {selector}")
    def _element(self, selector: dict = None, index: int = 0, link_text: str = None):
        self.logger.info("Find element: {}".format(selector))
        by = None
        if link_text:
            by = By.LINK_TEXT
            selector = link_text
        elif 'css' in selector.keys():
            by = By.CSS_SELECTOR
            selector = selector['css']
        elif 'xpath':
            by = By.XPATH
        return self.driver.find_elements(by, selector)[index]

    @allure.step("Поиск элемента checkbox в таблице: {selector}")
    def _find_element_checkbox_in_table(self, selector: dict, value_text: str):
        self.logger.info("Find element checkbox in table: {}".format(selector))
        by = By.CSS_SELECTOR
        selector_css = selector['css']
        a = self.driver.find_elements(by, selector_css)
        for i in a:
            if i.text == value_text:
                print(f"Элемент найден, это:", i.text)
                return i.find_element(by, 'input[type=checkbox]')
            else:
                print(f"Элемент не найден, это:", i.text)

    @allure.step("Нажимаем на checkbox найденного элемента")
    def _click_checkbox_in_table(self, element_object):
        self.logger.info("Clicking checkbox element: {}".format(element_object))
        element_object.click()

    @allure.step("Выбираем из списка значение - {value}, в элементе: {selector}")
    def _select_by_value(self, selector, value, index=0):
        self.logger.info("Select by value {} element: {}".format(value, selector))
        select = Select(self._element(selector, index))
        select.select_by_visible_text(value)

    @allure.step("Выбираем значение, radio button: {selector}")
    def _radio_button_value(self, selector: dict = None, index: int = 0):
        pass

    @allure.step("Confirm accept element!")
    def _confirm_accept(self):
        self.logger.info("Confirm accept element!")
        confirm = self.driver.switch_to.alert
        confirm.accept()

    # @allure.step("Нажимаем на элемент: {selector}")
    # def _click(self, selector, index=0):
    #     self.logger.info("Clicking element: {}".format(selector))
    #     ActionChains(self.driver).move_to_element(self._element(selector, index)).click().perform()

    def _click(self, selector, index=0, wait=15):
        try:
            WebDriverWait(self.driver, wait).until(EC.visibility_of(self._element(selector, index))).click()
            return self
        except TimeoutException:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name='screenshot_image',
                attachment_type=allure.attachment_type.PNG)
            raise TimeoutException

    @allure.step("Вводим значение {value}, в поле input - {selector}")
    def _input(self, selector, value, index=0):
        self.logger.info("Input {} in input {}".format(value, selector))
        element = self._element(selector, index)
        element.clear()
        element.send_keys(value)

    # @allure.step("Ждем появление элемента: {selector}")
    # def _wait_for_visible(self, selector, link_text=None, index=0, wait=15):
    #     self.logger.info("Wait for visible element: {}".format(selector))
    #     return WebDriverWait(self.driver, wait).until(EC.visibility_of(self._element(selector, index, link_text)))

    def _wait_for_visible(self, selector, link_text=None, index=0, wait=15):
        try:
            WebDriverWait(self.driver, wait).until(EC.visibility_of(self._element(selector, index, link_text)))
            return self
        except TimeoutException:
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name='screenshot_image',
                attachment_type=allure.attachment_type.PNG)
            raise TimeoutException

    @allure.step("Ждем состояние clickable элемента: {selector}")
    def _wait_to_be_clickable(self, selector, link_text=None, index=0, wait=10):
        self.logger.info("Wait to be clickable element: {}".format(selector))
        return WebDriverWait(self.driver, wait).until(EC.element_to_be_clickable(self._element(selector, index, link_text)))

    @allure.step("Получаем текст элемента: {selector}")
    def _get_element_text(self, selector, index=0, wait=15):
        self.logger.info("Get element text: {}".format(selector))
        self._wait_for_visible(selector, index, wait)
        return self._element(selector, index).text

    @allure.step("Открываем url: {url}")
    def _go_to(self, url):
        self.logger.info("Opening url: {}".format(url))
        return self.driver.get(url)

