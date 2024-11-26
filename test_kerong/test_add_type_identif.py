# Тип идентификатора. Создание карточки

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_add_type_identif import add_type_ident


def test_add_type_ident(browser):

    # авторизация
    authorization(browser)

    # создание типа идентиф
    add_type_ident(browser)
