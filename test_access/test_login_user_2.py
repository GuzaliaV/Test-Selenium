# Права доступа. Добавить пользователя. User_2


from browser_setup import browser
from test_access.test_func_1.test_func_login_user_2 import login_user_2


def test_login_user_2(browser):

    # User_2
    login_user_2(browser)

