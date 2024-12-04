# Права доступа. Добавить пользователя. User_5


from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_access.test_func_1.test_func_add_user_5 import user_5


def test_user_5(browser):

    # Вызов функции авторизации
    authorization(browser)

    # User_5
    user_5(browser)


