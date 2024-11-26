# Kerong Api. Редактирование соединения, без синхронизации

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_edit_kerong_api_not_synchr import edit_kerong_not_synchr


def test_edit_kerong(browser):

    # авторизация
    authorization(browser)

    # редактирование керонг
    edit_kerong_not_synchr(browser)



