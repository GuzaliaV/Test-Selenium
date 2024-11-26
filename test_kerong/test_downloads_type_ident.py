# Тип идентификатора. Загрузка файла

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_downloads_type_ident import downloads_type_ident



def test_downloads_type_ident(browser):

    #авторизация
    authorization(browser)

    # загрузка файла
    downloads_type_ident(browser)