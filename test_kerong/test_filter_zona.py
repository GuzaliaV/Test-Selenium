# Зоны. Фильтр

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_filter_zona import filter_zona


def test_filter_zona(browser):

    # авторизация
    authorization(browser)

    # фильтры
    filter_zona(browser)