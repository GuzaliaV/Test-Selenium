# Мониторинг. Зона. Открыть замок внутри ячейки


from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_open_lock_in_lock import open_lock_in_lock



def test_open_lock_in_lock(browser):

    # авторизация
    authorization(browser)

    # Открыть ячейку
    open_lock_in_lock(browser)