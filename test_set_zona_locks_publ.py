# создание зоны и добаление набора замков в публ зону

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_add_zone_publ import add_zone_publ
from test_func.test_func_add_lock_publ import add_lock_publ


def test_zona_locks_publ(browser):

    #авторизация
    authorization(browser)

    # создание зоны
    add_zone_publ(browser)

    # создание замков
    add_lock_publ(browser)