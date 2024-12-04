# Идентификаторы. Добавление идентиф и редактирование

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_edit_identif import edit_ident


def test_edit_ident(browser):

    #авторизация
    authorization(browser)

    #создание и редактирование типа идентиф
    edit_ident(browser)