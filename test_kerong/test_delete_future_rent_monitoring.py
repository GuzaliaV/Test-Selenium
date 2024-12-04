# Мониторинг. Зона. Выбрать свободную ячейку. Создать аренду на следующий день.

from browser_setup import browser
from test_kerong.test_authorization import authorization
from test_func.test_func_delete_future_rent_monitoring import delete_future_rent_monitoring


def test_delete_future_rent_monitoring(browser):

    # авторизация
    authorization(browser)

    # удалить будущую аренду
    delete_future_rent_monitoring(browser)