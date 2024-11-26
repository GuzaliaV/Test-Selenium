# Замки и ячейки. Создание набора замков для приватной зоны

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_add_lock_priv import add_lock_priv


def test_add_lock_priv(browser):

    #авторизация
    authorization(browser)

    #создание замков
    add_lock_priv(browser)