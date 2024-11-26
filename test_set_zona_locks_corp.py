# создание зоны и добаление набора замков в корп зону

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_add_zone_corp import add_zone_corp
from test_func.test_func_add_lock_corp import add_lock_corp



def test_zona_locks_corp(browser):

    #авторизация
    authorization(browser)

    # создание зоны
    add_zone_corp(browser)

    # создание замков
    add_lock_corp(browser)