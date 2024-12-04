# Права доступа. Добавить пользователя. User_6


from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_access.test_func_1.test_func_add_user_6 import user_6


def test_user_6(browser):

    # Вызов функции авторизации
    authorization(browser)

    # User_6
    user_6(browser)


