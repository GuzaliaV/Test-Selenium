# Мониторинг. Открыть ячейку

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_open_lock import open_lock


def test_open_lock(browser):

    # авторизация
    authorization(browser)

    # открытие ячейки
    open_lock(browser)
