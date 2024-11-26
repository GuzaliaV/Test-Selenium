# Мoниторинг. Зона. Открыть - По статусу - Все ячейки

from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import name_zone_publ

from time import sleep


def open_lock_all(browser):
    print("Test open_lock_all")
    wait = WebDriverWait(browser, 20)

    # открыть мониторинг
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Мониторинг']"))).click()

    # Открыть зону
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//h2[text() = '{name_zone_publ}']"))).click()

    # количество ячеек
    cells = browser.find_elements(By.CLASS_NAME, 'lock-item-container')
    cell_count = len(cells)
    print(f'Общее количество ячеек: {cell_count}')

    # Нажимаем Открыть
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()= 'Открыть']"))).click()

    # По статусу
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'по статусу']"))).click()

    # Выбрать занятые ячейки
    wait.until(EC.element_to_be_clickable((By.ID, 'demo-simple-select-helper'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text() = 'Все']"))).click()

    # Открыть
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[text()= 'Открыть'])[2]"))).click()

    # Получаю текст уведомления
    notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
    if notifications:
        last_notification_text = notifications[-1].text
        print(f"Текст уведомления: {last_notification_text}")

    # Перебор всех перехваченных запросов
    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")
                print()
 #               pytest.fail()

def test_open_lock_all(browser):
    open_lock_all(browser)
