# Клиенты. Карточка клиента. Снять активность

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_deactivating_client import deactivating_client


def test_deactivating_client(browser):

    # Вызов функции авторизации
    authorization(browser)

    # снятие активности
    deactivating_client(browser)
