# Мониторинг. Открыть зону, получить список замков

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_open_zone_monitoring import open_monitor


def test_open_monitor(browser):

    # авторизация
    authorization(browser)

    # открытие зоны
    open_monitor(browser)