# Права доступа. Добавить пользователя. User_1


from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_access.test_func_1.test_func_add_user_1 import user_1


def test_user_1(browser):

    # Вызов функции авторизации
    authorization(browser)

    # User_1
    user_1(browser)


