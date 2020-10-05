from selenium.webdriver.common.by import By


# Проверка title загруженной страницы
# localhost/index.php?route=product/category&path=20, Refine search
def test_desktops_page_title(browser):
    browser.get(browser.url + "/index.php?route=product/category&path=20")
    assert "Desktops" in browser.title


# Проверка открытой категории Desktops
# localhost/index.php?route=product/category&path=20, Desktops
def test_desktops_page_category(browser):
    browser.get(browser.url + "/index.php?route=product/category&path=20")
    value_text = browser.find_element_by_css_selector('#content > h2').text
    assert "Desktops" == value_text


# Поиск Refine search
# localhost/index.php?route=product/category&path=20, Refine search
def test_desktops_page_search_value(browser):
    browser.get(browser.url + "/index.php?route=product/category&path=20")
    value_text = browser.find_element_by_css_selector('#content > h3').text
    assert value_text == str('Refine Search')


# Проверка списка сортировки, по умолчанию выбран Default
# /index.php?route=product/category&path=20
def test_page_desktops_sort(browser):
    browser.get(browser.url + "/index.php?route=product/category&path=20")
    el = browser.find_element(By.CSS_SELECTOR, "#input-sort")
    all_options = el.find_elements_by_tag_name("option")
    for option in all_options:
        if option.get_attribute("selected"):
            def_text = option.text
            assert def_text == "Default"


# Проверка кнопок отображения list или grid, состояние list default active
# /index.php?route=product/category&path=20
def test_page_desktops_list_grid(browser):
    browser.get(browser.url + "/index.php?route=product/category&path=20")
    grid_attr = browser.find_element(By.CSS_SELECTOR, "#grid-view").get_attribute('class')
    assert grid_attr == "btn btn-default active"
    list_button = browser.find_element(By.CSS_SELECTOR, "#list-view")
    list_button.click()
    list_attr = list_button.get_attribute('class')
    assert list_attr == "btn btn-default active"


# Проверка в блоке list group, что атрибут у Desktops - active
# /index.php?route=product/category&path=20
def test_page_desktops_list_group(browser):
    browser.get(browser.url + "/index.php?route=product/category&path=20")
    grid_attr = browser.find_element(By.CSS_SELECTOR, "#column-left > div.list-group > a.list-group-item.active")
    assert grid_attr.get_attribute('class') == "list-group-item active"
