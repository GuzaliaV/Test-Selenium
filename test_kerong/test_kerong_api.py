# авторизация и настройка керонг апи

from test_kerong.test_authorization import authorization
from test_func.test_func_add_kerong_api import add_kerong
from browser_setup import browser


def test_add_kerong(browser):

    # авторизация
    authorization(browser)

    # создание соединения керонг апи
    add_kerong(browser)



