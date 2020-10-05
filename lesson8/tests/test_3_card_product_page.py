from selenium.webdriver.common.by import By


# Проверка в breadcrumb tablets, и samsung
# /index.php?route=product/product&path=57&product_id=49
def test_page_samsung_list_group(browser):
    browser.get(browser.url + "/index.php?route=product/product&path=57&product_id=49")
    tablets = browser.find_element(By.CSS_SELECTOR, "#product-product > ul > li:nth-child(2)").text
    assert tablets == "Tablets"
    samsung = browser.find_element(By.CSS_SELECTOR, "#product-product > ul > li:nth-child(3)").text
    assert samsung == "Samsung Galaxy Tab 10.1"


# Проверка title на странице
# /index.php?route=product/product&path=57&product_id=49
def test_page_samsung_title(browser):
    browser.get(browser.url + "/index.php?route=product/product&path=57&product_id=49")
    assert "Samsung Galaxy Tab 10.1" in browser.title


# Проверка nav-tabs description
# /index.php?route=product/product&path=57&product_id=49
def test_page_samsung_nav_tabs_description(browser):
    browser.get(browser.url + "/index.php?route=product/product&path=57&product_id=49")
    description = browser.find_element(By.CSS_SELECTOR,
                                       "#content > div > div.col-sm-8 > ul.nav.nav-tabs > li:nth-child(1)")
    assert description.text == "Description"
    assert description.get_attribute('class') == "active"


# Проверка nav-tabs на переключение reviews
# /index.php?route=product/product&path=57&product_id=49
def test_page_samsung_nav_tabs_reviews(browser):
    browser.get(browser.url + "/index.php?route=product/product&path=57&product_id=49")
    reviews = browser.find_element(By.CSS_SELECTOR,
                                   "#content > div > div.col-sm-8 > ul.nav.nav-tabs > li:nth-child(2)")
    reviews.click()
    assert reviews.get_attribute('class') == "active"
    header_reviews = browser.find_element(By.CSS_SELECTOR, "#form-review > h2")
    assert header_reviews.text == "Write a review"


# Проверка col-sm-4 на переключение reviews
# /index.php?route=product/product&path=57&product_id=49
def test_page_samsung_description(browser):
    browser.get(browser.url + "/index.php?route=product/product&path=57&product_id=49")
    description = browser.find_element(By.CSS_SELECTOR, "#content > div > div.col-sm-4 > h1")
    assert description.text == "Samsung Galaxy Tab 10.1"
