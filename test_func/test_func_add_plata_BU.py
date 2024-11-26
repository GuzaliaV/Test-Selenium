# Платы. Создание платы BU

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import ip_plata, name_BU_text
from test_func.func_search import search_line

from time import sleep


def add_card_BU(browser):
    wait = WebDriverWait(browser, 20)

    # Клик на Справочники
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Справочники']"))).click()

    # Клик по Платы
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='table-item'])[2]"))).click()

    # Добавить KR-BU
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Добавить KR-BU']"))).click()

    # Ввести наименование
    name_plata = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='outlined-basic'])[2]")))
    name_plata.send_keys(name_BU_text)

    # Выбрать тип KR-BU
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@id='demo-simple-select-helper'])[1]"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@data-value='KR-BU']"))).click()

    # Ввести IP
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id='outlined-basic'])[3]"))).send_keys(ip_plata)

    # Выбрать тип KR-CU
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@id='demo-simple-select-helper'])[2]"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//li[@data-value='CU_48']"))).click()

    # Сохранить карточку
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Сохранить']"))).click()
    sleep(0.1)
    print(f"Плата '{name_BU_text}' создана")

    # Получаю текст уведомление
    browser.implicitly_wait(10)
    notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
    if notifications:
        last_notification_text = notifications[-1].text
        print(f"Текст уведомления: {last_notification_text}")

    # Проверка наличия созданной карточки
    if search_line(browser, name_BU_text):
        print()
    else:
        print(f"'{name_BU_text}' - не найден")

    # Проверка на наличие ошибок в запросах
    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code}. Текст ошибки: {error_message}")

# Выполнение функции
def test_add_card_BU(browser):
    add_card_BU(browser)

