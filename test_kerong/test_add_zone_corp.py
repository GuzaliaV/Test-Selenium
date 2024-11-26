# Зоны. Создание корпоративной зоны

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_add_zone_corp import add_zone_corp


def test_add_zone_corp(browser):

    #авторизация
    authorization(browser)

    #создание зоны
    add_zone_corp(browser)