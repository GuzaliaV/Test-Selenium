# Kerong Api. Строка Поиска

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_search_kerong_api import search_kerong


def test_search_kerong(browser):

    # Авторизация
    authorization(browser)

    # поиск
    search_kerong(browser)



