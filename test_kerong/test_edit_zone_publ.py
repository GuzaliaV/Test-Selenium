# Зоны. Добавление публичной зоны и редактирование

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_edit_zone_publ import edit_zone_publ



def test_edit_zone_publ(browser):

    #авторизация
    authorization(browser)

    #создание и редактирование зоны
    edit_zone_publ(browser)