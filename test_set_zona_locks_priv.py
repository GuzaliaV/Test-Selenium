# создание зоны и добаление набора замков в приватную зону

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_add_zone_private import add_zone_private
from test_func.test_func_add_lock_priv import add_lock_priv



def test_zona_locks_priv(browser):

    #авторизация
    authorization(browser)

    # создание зоны
    add_zone_private(browser)

    # создание замков
    add_lock_priv(browser)