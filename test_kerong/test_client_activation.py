# Клиенты. Карточка клиента. Вернуть активность

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_client_activation import client_activation


def test_client_activation(browser):

    # Вызов функции авторизации
    authorization(browser)

    # вернуть активность
    client_activation(browser)
