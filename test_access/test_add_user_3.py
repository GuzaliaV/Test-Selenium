# Права доступа. Добавить пользователя. User_3


from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_access.test_func_1.test_func_add_user_3 import user_3


def test_user_3(browser):

    # Вызов функции авторизации
    authorization(browser)

    # User_3
    user_3(browser)


