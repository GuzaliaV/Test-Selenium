# создание карточки керонг, платы BU, CU, замков, ТИ, идентиф

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_add_kerong_api import add_kerong

from test_func.test_func_add_plata_BU import add_card_BU
from test_func.test_func_add_plata_CU import add_card_CU

from test_func.test_func_add_zone_private import add_zone_private
from test_func.test_func_add_lock_priv import add_lock_priv

from test_func.test_func_add_zone_corp import add_zone_corp
from test_func.test_func_add_lock_corp import add_lock_corp

from test_func.test_func_add_zone_publ import add_zone_publ
from test_func.test_func_add_lock_publ import add_lock_publ

from test_func.test_func_add_type_identif import add_type_ident
from test_func.test_func_add_identif import add_ident
from test_func.test_func_add_client import add_client


def test_add_all(browser):
    print()
    # авторизация
    authorization(browser)

    # соединение керонг
    add_kerong(browser)
    print()

    # создание BU
    add_card_BU(browser)
    print()

    # создание CU
    add_card_CU(browser)
    print()

    # создание зоны приватной
    add_zone_private(browser)
    print()

    # создание замков
    add_lock_priv(browser)
    print()

    # создание зоны корп
    add_zone_corp(browser)
    print()

    # создание замков
    add_lock_corp(browser)
    print()

    # создание зоны публ
    add_zone_publ(browser)
    print()

    # создание замков
    add_lock_publ(browser)
    print()

    # создание типа идентиф
    add_type_ident(browser)
    print()

    # создание идентиф
    add_ident(browser)
    print()

    # добавление клиента
    add_client(browser)
    print()