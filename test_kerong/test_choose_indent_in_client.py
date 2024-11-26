# Клиенты. Карточка клиента. Выбрать идентификатор

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_choose_indent_in_client import choose_indent_in_client


def test_choose_indent_in_client(browser):

    # Авторизация
    authorization(browser)

    # Выбрать идентификатор в карточке Клиента
    choose_indent_in_client(browser)

