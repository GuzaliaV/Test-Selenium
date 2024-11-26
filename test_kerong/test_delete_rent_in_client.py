# Клиенты. Карточка клиента. Удаление доступа к ячейкам (приватная аренда)

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_delete_rent_in_client import delete_rent_in_client
from test_func.test_func_add_privat_rent_ident_in_client import add_privat_rent_ident_in_client


def test_delete_rent_in_client(browser):

    # Вызов функции авторизации
    authorization(browser)

    # создание аренды
    add_privat_rent_ident_in_client(browser)

    # удаление доступа
    delete_rent_in_client(browser)


