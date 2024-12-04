# Права доступа. Добавить пользователя. User_2


from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_access.test_func_1.test_func_add_user_2 import user_2


def test_user_2(browser):

    # Вызов функции авторизации
    authorization(browser)

    # User_2
    user_2(browser)


