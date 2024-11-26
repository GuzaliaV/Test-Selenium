# Клиенты. Фильтр по полу -  женский пол

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_filter_female import filter_female


def test_filter_female(browser):

    # Вызов функции авторизации
    authorization(browser)

    # фильтрация
    filter_female(browser)
