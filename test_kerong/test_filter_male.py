# Клиенты. Фильтр по полу - мужской пол

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_filter_male import filter_male


def test_filter_male(browser):

    # Вызов функции авторизации
    authorization(browser)

    # фильтрация
    filter_male(browser)
