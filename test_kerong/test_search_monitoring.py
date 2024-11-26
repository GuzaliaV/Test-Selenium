# Мониторинг. Зона. Строка поиска

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_search_monitoring import search_monitoring


def test_search_monitoring(browser):

    # авторизация
    authorization(browser)

    # поиск
    search_monitoring(browser)