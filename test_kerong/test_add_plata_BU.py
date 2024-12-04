# Платы. Создание платы BU

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_add_plata_BU import add_card_BU

# import pytest
# from config import set_random_name, name_BU_text
#
# # Фикстура для создания случайного имени
# @pytest.fixture
# def random_name_BU_text():
#     set_random_name()
#     return name_BU_text

def test_add_card_BU(browser):

    # авторизация
    authorization(browser)

    # создание платы BU
    add_card_BU(browser)