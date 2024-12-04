# Клиенты. Добавить идентификатор в карточке Клиента

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_add_ident_in_client import add_ident_in_client


def test_func_edit_ident_in_client(browser):

    # Авторизация
    authorization(browser)

    # Добавить идентификатор в карточке Клиента
    add_ident_in_client(browser)



