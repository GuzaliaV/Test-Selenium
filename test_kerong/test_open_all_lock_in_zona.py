# Мoниторинг. Зона. Открыть - По статусу - Все ячейки

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_open_all_lock_in_zona import open_lock_all

def test_open_lock_all(browser):

    # авторизация
    authorization(browser)

    # Открытие всех ячеек
    open_lock_all(browser)