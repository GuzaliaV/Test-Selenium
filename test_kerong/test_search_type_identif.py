# Типы идентификаторов. Строка Поиска

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_search_type_identif import search_type_identif



def test_search_type_identif(browser):

    # авторизация
    authorization(browser)

    # поиск
    search_type_identif(browser)