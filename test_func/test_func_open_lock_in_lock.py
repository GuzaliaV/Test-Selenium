# Мониторинг. Зона. Открыть замок внутри ячейки

from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import name_zone_private

from time import sleep


def open_lock_in_lock(browser):
    wait = WebDriverWait(browser, 20)

    # открыть мониторинг
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Мониторинг']"))).click()

    # выбрать зону
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//h2[text() = '{name_zone_private}']"))).click()
    sleep(2)

    # Все ячейки
    cells = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "lock-item-container")))
    print(f"Кол-во ячеек: {len(cells)}")

    closed_opened = False
    for cell in cells:
        # номер ячейки
        cell_title = cell.find_element(By.CLASS_NAME, "title").text
        print(cell_title, end=", ")

        # Замки со статусом "Закрыт"
        closed_icons = cell.find_elements(By.XPATH, ".//div[@aria-label='Закрыт']")
        if closed_icons:
            try:
                # Клик на закрытую ячейку
                browser.execute_script("arguments[0].click();", closed_icons[0])

                # "Открыть" замок
                open_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[text()= 'Открыть'])[2]")))
                open_button.click()
                sleep(2)

                # Получаю текст уведомления
                notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
                if notifications:
                    last_notification_text = notifications[-1].text
                    print(f"Текст уведомления: {last_notification_text}, {cell_title}")

                closed_opened = True
                break
            except Exception as e:
                print(f"Ошибка при клике на 'Закрыт': {str(e)}")

    # Если все ячейки открыты
    if not closed_opened:
        for cell in cells:

            # номер ячейки
            cell_title = cell.find_element(By.CLASS_NAME, "title").text

            open_icons = cell.find_elements(By.XPATH, ".//div[@aria-label='Открыт']")
            if open_icons:
                try:

                    # Клик на открытую ячейку
                    browser.execute_script("arguments[0].click();", open_icons[0])

                    # "Открыть"
                    open_button = wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[text()= 'Открыть'])[2]")))
                    open_button.click()
                    sleep(2)

                    # Получаю текст уведомления
                    notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
                    if notifications:
                        last_notification_text = notifications[-1].text
                        print(f"Текст уведомления: {last_notification_text}, {cell_title}")

                    break
                except Exception as e:
                    print(f"Ошибка при клике на 'Открыт': {str(e)}")

    # Перебор всех перехваченных запросов
    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101, 201}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")

def test_open_lock_in_lock(browser):
    open_lock_in_lock(browser)
