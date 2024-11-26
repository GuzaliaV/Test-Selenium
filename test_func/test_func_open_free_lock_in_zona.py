# Мoниторинг. Зона. Открыть - По статусу - Свободные ячейки

from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from config import name_zone_publ

from selenium.webdriver.common.keys import Keys
from time import sleep



def click_empty_space(browser):
    actions = ActionChains(browser)
    actions.move_by_offset(0, 0).click().perform()

def open_lock_free(browser):
    print("Test open_lock_free")
    wait = WebDriverWait(browser, 20)
    actions = ActionChains(browser)

    # открыть мониторинг
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Мониторинг']"))).click()
    sleep(0.1)

    # Открыть зону
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//h2[text() = '{name_zone_publ}']"))).click()
    sleep(0.1)

    # количество ячеек
    cells = browser.find_elements(By.CLASS_NAME, 'lock-item-container')
    cell_count = len(cells)
    print(f'Общее количество ячеек: {cell_count}')

    lock_all = browser.find_elements(By.CLASS_NAME, "lock-item-container")
    locks_num = 0

    for l in lock_all:
        try:
            lock_name_free = l.find_element(By.XPATH, ".//div[@class='free']").text

            if lock_name_free:
                locks_num += 1

                # Нажимаем Открыть
                wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()= 'Открыть']"))).click()

                # Открываем ячейку по статусу Занятые
                wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'по статусу']"))).click()
                wait.until(EC.element_to_be_clickable((By.ID, 'demo-simple-select-helper'))).click()
                wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text() = 'Свободные']"))).click()
                wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[text()= 'Открыть'])[2]"))).click()
                actions.send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()
                sleep(0.2)

                # Получаю текст уведомления
                notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
                if notifications:
                    last_notification_text = notifications[-1].text
                    print(f"Текст уведомления: {last_notification_text}")

        except:
            pass
    print(f"Количество свободных ячеек: {locks_num}")

    # Перебор всех перехваченных запросов
    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101, 201}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")
                print()
 #               pytest.fail()


def test_open_lock_free(browser):
    open_lock_free(browser)
