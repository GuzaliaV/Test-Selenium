# удаление идентификатора в карточке клиента

from test_func.test_func_delete_ident_in_client import delete_ident_in_client
from test_kerong.test_authorization import authorization
from browser_setup import browser


def test_delete_ident(browser):

    #авторизация
    authorization(browser)

    # удаление
    delete_ident_in_client(browser)