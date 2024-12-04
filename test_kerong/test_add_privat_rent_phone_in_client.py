# Клиенты. Открыть карточку клиента. Добавить доступ к ячейкам по 'телефон + код'

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_add_ident_in_client import add_ident_in_client
from test_func.test_func_add_privat_rent_phone_in_client import add_privat_rent_phone_in_client


def test_add_privat_rent_phone_in_client(browser):

    # Авторизация
    authorization(browser)

    # Добавить идентификатор в карточке Клиента
    add_ident_in_client(browser)
    print()

    # добавить доступ
    add_privat_rent_phone_in_client(browser)

