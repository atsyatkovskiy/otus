import time
from selenium.webdriver.common.by import By


# Проверка, на главное странице вывод 4-х товаров
# localhost/, #content
def test_home_page_content(browser):
    browser.get(browser.url)
    num_product = browser.find_element_by_css_selector('#content > div.row')
    for i in range(0, 4):
        i += 1
        num_product.find_element_by_css_selector(f'#content > div.row > div:nth-child({i})')


# Проверка на строку поиска, и клик кнопки find
# localhost/, search
def test_home_page_search(browser):
    browser.get(browser.url)
    search_input = browser.find_element_by_css_selector('#search > input')
    search_input.send_keys('123')
    search_button = browser.find_element_by_css_selector('#search > span')
    search_button.click()


# Проверка элементов в меню
# localhost/, num menu (8 elements)
def test_home_page_menu(browser):
    browser.get(browser.url)
    menu_items = browser.find_elements_by_css_selector("ul.navbar-nav > li")
    assert len(menu_items) == 8, "Неверное количество элементов меню"


# Проверка значения в корзине, что она пустая
# localhost/, basket value
def test_home_page_basket_value(browser):
    browser.get(browser.url)
    value = browser.find_element_by_css_selector('#cart-total').text
    assert value == "0 item(s) - $0.00"


# Проверка нижнего блока навигации
# localhost/, #row
def test_home_page_row(browser):
    browser.get(browser.url)
    num_product = browser.find_element_by_css_selector('body > footer > div > div')
    for i in range(0, 4):
        i += 1
        text = num_product.find_element_by_css_selector(f'body > footer > div > div > div:nth-child({i})').text
        assert rows[i - 1] == text


rows = ["Information\nAbout Us\nDelivery Information\nPrivacy Policy\nTerms & Conditions",
        "Customer Service\nContact Us\nReturns\nSite Map",
        "Extras\nBrands\nGift Certificates\nAffiliate\nSpecials",
        "My Account\nMy Account\nOrder History\nWish List\nNewsletter"]