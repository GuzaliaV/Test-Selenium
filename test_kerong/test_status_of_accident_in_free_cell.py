# Мониторинг. Зона. Выбрать свободную ячейку. Установить статус 'Авария'

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_status_of_accident_in_free_cell import status_of_accident_in_free_cell

def test_status_of_accident_in_free_cell(browser):

    # авторизация
    authorization(browser)

    # Статус авария
    status_of_accident_in_free_cell(browser)