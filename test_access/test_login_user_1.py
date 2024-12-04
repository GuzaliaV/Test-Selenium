# Права доступа. Добавить пользователя. User_1


from browser_setup import browser
from test_access.test_func_1.test_func_login_user_1 import login_user_1


def test_login_user_1(browser):

    # User_1
    login_user_1(browser)

