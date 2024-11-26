# Платы. Строка Поиска. СU платы

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_search_plata_CU import search_plata_CU


def test_search_plata_CU(browser):

    # авторизация
    authorization(browser)

    # поиск
    search_plata_CU(browser)