# Мониторинг. Зона. Выбрать занятую ячейку. Открыть замок


from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_open_lock_rent_in_cell import open_lock_rent_in_cell

def test_open_lock_rent_in_cell(browser):

    # Вызов функции авторизации
    authorization(browser)

    # открыть замок
    open_lock_rent_in_cell(browser)