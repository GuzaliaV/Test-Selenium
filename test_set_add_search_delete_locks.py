# Авторизация
# Добавить замки и ячейки
# Поиск
# Удаление набора

from test_func.test_func_add_search_delete_lock import add_search_delete_locks
from test_kerong.test_authorization import authorization
from browser_setup import browser

def test_add_search_delete_lock(browser):

    print()
    # авторизация
    authorization(browser)

    # создание, поиск,  удаление набора замков
    add_search_delete_locks(browser)