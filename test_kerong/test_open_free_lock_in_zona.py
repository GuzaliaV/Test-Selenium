# Мoниторинг. Зона. Открыть - По статусу - Свободные ячейки

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_open_free_lock_in_zona import open_lock_free



def test_open_lock_free(browser):

    #авторизация
    authorization(browser)

    # Открытие свободных ячейки
    open_lock_free(browser)