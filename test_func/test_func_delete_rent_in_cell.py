# Мониторинг. Зона. Выбрать занятую ячейку. Снять аренду

from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from config import name_zone_private
from termcolor import cprint
from time import sleep


def delete_rent_in_cell(browser):
    wait = WebDriverWait(browser, 10)
    actions = ActionChains(browser)

    cprint("Мониторинг. Зона. Выбрать занятую ячейку. Снять аренду / test_func_delete_rent_in_cell", "yellow")

    # открыть мониторинг
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Мониторинг']"))).click()

    # выбрать зону
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//h2[text() = '{name_zone_private}']"))).click()

    # Все ячейки
    cells = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "lock-item-container")))
    print(f"В зоне '{name_zone_private}' кол-во ячеек: {len(cells)}")

    rent_cell = False
    for cell in cells:

        # номер ячейки
        cell_title = cell.find_element(By.CLASS_NAME, "title").text

        # занятые ячейки
        rent = cell.find_elements(By.XPATH, "//div[@class ='rent']")
        if rent:
            try:
                # Клик на занятую ячейку
                browser.execute_script("arguments[0].click();", rent[0])
                sleep(1)
                s = browser.find_element(By.XPATH, "//div/h2").text
                print(f"Снять аренду с '{s}'")

                # клик на Снять аренду
                wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Снять аренду']"))).click()
                actions.send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()
                sleep(1)

                # Получаю текст уведомления
                notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
                if notifications:
                    last_notification_text = notifications[-1].text
                    print(f"Текст уведомления: {last_notification_text}")

                for request in browser.requests:
                    if request.response:
                        if request.response.status_code not in {200, 101, 201}:
                            error_message = request.response.body.decode('utf-8')
                            print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")
                rent_cell = True
                break
            except Exception as e:
                print(f"Ошибка: {str(e)}")

    if not rent_cell:
        print(f"Все ячейки свободны")

        # Получаю текст уведомления
        notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
        if notifications:
            last_notification_text = notifications[-1].text
            print(f"Текст уведомления: {last_notification_text}, {cell_title}")

        for request in browser.requests:
            if request.response:
                if request.response.status_code not in {200, 101}:
                    error_message = request.response.body.decode('utf-8')
                    print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")

                    break


def test_delete_rent_in_cell(browser):
    delete_rent_in_cell(browser)