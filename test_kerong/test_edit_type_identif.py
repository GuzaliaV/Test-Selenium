# Идентификаторы. Добавление идентиф и редактирование

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_edit_type_identif import edit_type_ident


def test_edit_type_ident(browser):

    #авторизация
    authorization(browser)

    #создание и редактирование типа идентиф
    edit_type_ident(browser)