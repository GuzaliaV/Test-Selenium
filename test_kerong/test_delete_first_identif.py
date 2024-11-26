#  Идентификаторы. Удаление первого в списке идентификатора

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_delete_first_identif import delete_first_identif


def test_delete_first_identif(browser):

    #авторизация
    authorization(browser)

    # удаление
    delete_first_identif(browser)