# Мониторинг. Зона. Фильтр - Свободные

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_filter_free_lock_monitoring import filter_free_lock_monitoring


def test_filter_free_lock_monitoring(browser):

    # авторизация
    authorization(browser)

    # фильтр на свободные ячейки
    filter_free_lock_monitoring(browser)