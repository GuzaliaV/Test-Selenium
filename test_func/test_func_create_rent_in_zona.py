# Мониторинг. Зона. Создать аренду


from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import name_zone_private

from time import sleep
from datetime import datetime


def create_rent_in_zona(browser):
    wait = WebDriverWait(browser, 20)

    # открыть мониторинг
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Мониторинг']"))).click()

    # выбрать зону
    wait.until(EC.element_to_be_clickable((By.XPATH, f"//h2[text() = '{name_zone_private}']"))).click()
    sleep(1)

    # Все ячейки
    cells = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "lock-item-container")))
    print(f"Кол-во ячеек: {len(cells)}")

    free_cell = False
    for cell in cells:

        # Свободные ячейки
        free = cell.find_element(By.XPATH, "//div[@class ='free']").text

        if free:
            try:
                # номер первой найденной свободной ячейки
                cell_title = cell.find_element(By.CLASS_NAME, "title").text
                print(f"Номер первой в списке свободной ячейки '{cell_title}'")

                # клик на "создать аренду"
                wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Создать аренду']"))).click()
#                sleep(1)

                # выбрать идентификатор
                wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id = 'demo-simple-select-helper']"))).click()
#                sleep(1)
                wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul:nth-child(1) li"))).click()
#                sleep(1)

                # ввести номер ячейки
                num = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[2]")))
                num.send_keys(cell_title)
#                sleep(1)

                # Начало периода
                wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class = 'MuiButtonBase-root MuiIconButton-root MuiIconButton-edgeEnd MuiIconButton-sizeMedium css-slyssw']"))).click()
#                sleep(1)
                wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class = 'MuiButtonBase-root MuiPickersDay-root MuiPickersDay-dayWithMargin MuiPickersDay-today css-9e71xu']"))).click()
#                sleep(1)

                # Конец периода
                wait.until(EC.element_to_be_clickable((By.XPATH,"(//button[@class = 'MuiButtonBase-root MuiIconButton-root MuiIconButton-edgeEnd MuiIconButton-sizeMedium css-slyssw'])[2]"))).click()
#                sleep(1)
                wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class = 'MuiButtonBase-root MuiPickersDay-root MuiPickersDay-dayWithMargin MuiPickersDay-today css-9e71xu']"))).click()
#                sleep(1)

                # начальное время
                input_element = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH,"(//input[@class = 'MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputAdornedEnd css-1uvydh2'])[2]")))
                input_element.click()
                input_value = input_element.get_attribute("value")
                hours, minutes = map(int, input_value.split(':'))

                # +1 час от начального времени
                hours += 1
                if hours == 24:
                    hours = 0
                new_time = f"{hours:02}:{minutes:02}"
#                sleep(1)

                # конечное время
                time_end = wait.until(EC.element_to_be_clickable((By.XPATH,"(//input[@class = 'MuiInputBase-input MuiOutlinedInput-input MuiInputBase-inputAdornedEnd css-1uvydh2'])[4]")))
                time_end.click()
                time_end.send_keys(new_time)
#                sleep(1)

                # Создать аренду
                wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[text() = 'Создать аренду'])[2]"))).click()
                sleep(1)

                # Получение текущей даты и времени
                current_datetime = datetime.now().strftime("%d.%m.%Y")
                print(f"Создана аренда на ячейку '{cell_title}', на {current_datetime} с {input_value} по {new_time}")

                # Получаю текст уведомления
                notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
                if notifications:
                    last_notification_text = notifications[-1].text
                    print(f"Текст уведомления: {last_notification_text}")

                for request in browser.requests:
                    if request.response:
                        if request.response.status_code not in {200, 101}:
                            error_message = request.response.body.decode('utf-8')
                            print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")

                free_cell = True
                break
            except Exception as e:
                print(f"Ошибка: {str(e)}")


    if not free_cell:
        for cell in cells:

            # номер ячейки
            cell_title = cell.find_element(By.CLASS_NAME, "title").text

            print(f"Все ячейки заняты {cell_title}")

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

def test_create_rent_in_zona(browser):
    create_rent_in_zona(browser)








