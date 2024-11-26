# Kerong Api. Загрузка файла

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_downloads_kerong_api import downloads_kerong



def test_downloads_kerong(browser):

    #авторизация
    authorization(browser)

    # загрузка файла
    downloads_kerong(browser)