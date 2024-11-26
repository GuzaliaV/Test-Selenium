# Добавление клиента. Редактирование. Снять активность. Вернуть активность. Поиск: По имени, По телефону, По идентификатору. Фильтры


from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_add_client import add_client
from test_func.test_func_client_activation import client_activation
from test_func.test_func_deactivating_client import deactivating_client
from test_func.test_func_search_client import search_client

from test_func.test_func_edit_client import edit_client
from test_func.test_func_filter_female import filter_female
from test_func.test_func_filter_male import filter_male
from test_func.test_func_filter_birthday import filter_birthday

def test_client(browser):

    # Вызов функции авторизации
    authorization(browser)

    # добавление клиента
    add_client(browser)
    print()

    # редактирование клиента
    edit_client(browser)
    print()

    # снятие активности
    deactivating_client(browser)
    print()

    # вернуть активность
    client_activation(browser)
    print()

    # поиск
    search_client(browser)
    print()

    # фильтрация Ж пол
    filter_female(browser)
    print()

    # фильтрация М пол
    filter_male(browser)
    print()

    # фильтрация ДР
    filter_birthday(browser)

