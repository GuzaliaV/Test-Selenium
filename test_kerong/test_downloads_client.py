# Клиенты. Загрузка файла

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_downloads_client import downloads_client



def test_downloads_client(browser):

    #авторизация
    authorization(browser)

    # загрузка файла
    downloads_client(browser)