# добавление CU платы и проверка наличия карточки

from test_func.test_func_add_plata_CU import add_card_CU
from test_kerong.test_authorization import authorization
from browser_setup import browser


def test_add_card_CU(browser):

    #авторизация
    authorization(browser)

    #создание CU платы
    add_card_CU(browser)