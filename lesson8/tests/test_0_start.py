import sys


# Проверка title, ссылки загруженной страницы
# localhost/, Refine search
def test_home_page(browser):
    browser.get(browser.url)
    assert "Your Store" in browser.title
    try:
        browser.find_element_by_link_text("OpenCart")
        print('Найден элемент с текстом ссылки')
    except:
        print('Не найден элемент с текстом ссылки')
        sys.exit(1)
