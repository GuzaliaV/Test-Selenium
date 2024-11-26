# Мoниторинг. Зона. Открыть - несколько ячейкек

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_open_some_lock_in_zona import open_lock_some



def test_open_lock_some(browser):

    # авторизация
    authorization(browser)

    # Открытие нескольких ячеек
    open_lock_some(browser)