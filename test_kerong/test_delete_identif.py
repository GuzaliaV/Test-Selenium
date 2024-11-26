#  Идентификаторы. Создание и удаление идентификатора

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_delete_identif import delete_ident


def test_delete_ident(browser):

    #авторизация
    authorization(browser)

    # удаление
    delete_ident(browser)