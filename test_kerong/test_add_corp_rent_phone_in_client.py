# Клиенты. Открыть карточку клиента. Добавить доступ к ячейкам на корп.зону , по 'телефон + код'

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_add_ident_in_client import edit_ident_in_client
from test_func.test_func_access_corporate_zone import access_corporate_zone
from test_func.test_func_add_corp_rent_phone_in_client import add_corp_rent_phone_in_client


def test_add_corp_rent_phone_in_client(browser):

    # Авторизация
    authorization(browser)

    # Добавить идентификатор в карточке Клиента
    edit_ident_in_client(browser)

    # Добавить доступ к зонам
    access_corporate_zone(browser)

    # добавить к ячейкам
    add_corp_rent_phone_in_client(browser)
