import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_button_add_to_basket(browser):
    browser.get(link)
    #time.sleep(4)
    rez = len(browser.find_elements_by_css_selector("form#add_to_basket_form button"))
    assert rez == 1, "Кнопка \"Добавить в корзину\" не найдена"
