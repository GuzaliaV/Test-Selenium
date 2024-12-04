# Мониторинг. Зона. Фильтр - Свободные, Занятые, Все

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_filter_monitoring import filter_rent_lock_monitoring, filter_free_lock_monitoring, filter_all_lock_monitoring


def test_filter_monitoring(browser):

    # авторизация
    authorization(browser)

    # фильтр свободные
    filter_free_lock_monitoring(browser)
    print()

    # фильтр занятые
    filter_rent_lock_monitoring(browser)
    print()

    # фильтр все
    filter_all_lock_monitoring(browser)
