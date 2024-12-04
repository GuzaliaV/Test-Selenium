# Мониторинг. Зона. Выбрать занятую ячейку. Снять аренду


from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_delete_rent_in_cell import delete_rent_in_cell

def test_delete_rent_in_cell(browser):

    # Вызов функции авторизации
    authorization(browser)

    # снять аренду
    delete_rent_in_cell(browser)