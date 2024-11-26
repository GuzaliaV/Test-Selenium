# Замки и ячейки. Создание набора замков, поиск, удаление

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_add_search_delete_lock import add_search_delete_locks


def test_add_search_delete_lock(browser):

    # авторизация
    authorization(browser)

    # создание, поиск,  удаление набора замков
    add_search_delete_locks(browser)