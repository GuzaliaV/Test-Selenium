# Типы идентификатора. Создание и удалиение ТИ

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_delete_type_identif import delete_type_ident


def test_delete_type_ident(browser):

    # авторизация
    authorization(browser)

    # удаление
    delete_type_ident(browser)