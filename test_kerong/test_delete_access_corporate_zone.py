# Клиенты. Карточка клиента. Удалить доступ в корп зону

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_delete_access_corporate_zone import delete_access
from test_func.test_func_access_corporate_zone import access_corporate_zone


def test_delete_ident(browser):

    # Вызов функции авторизации
    authorization(browser)

    # Добавить доступ
    access_corporate_zone(browser)

    # удаление доступа в корп зону
    delete_access(browser)