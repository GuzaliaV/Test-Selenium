# Права доступа. Добавить пользователя. User_4


from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_access.test_func_1.test_func_add_user_4 import user_4


def test_user_4(browser):

    # Вызов функции авторизации
    authorization(browser)

    # User_4
    user_4(browser)


