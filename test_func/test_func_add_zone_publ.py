# Зоны. Создание публичной зоны

from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from test_func.func_search import search_line
from config import name_zone_publ, num_from_publ, num_to_publ

from selenium.webdriver import Keys
from time import sleep


def add_zone_publ(browser):
    wait = WebDriverWait(browser, 20)

    # Клик на Справочники
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Справочники']"))).click()

    # Клик на Зоны
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='table-item'])[1]"))).click()

    # Клик на Добавить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class = 'UIbutton']"))).click()

    # Ввести наименование
    name_zone = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[2]")))
    name_zone.send_keys(name_zone_publ)

    # Номера От
    num1 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[3]")))
    num1.send_keys(Keys.CONTROL, "a")
    num1.send_keys(num_from_publ)
    sleep(0.1)

    # Номера До
    num2 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[4]")))
    num2.send_keys(Keys.CONTROL, "a")
    num2.send_keys(num_to_publ)
    sleep(0.1)

    # Режим доступа
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id = 'demo-simple-select-helper']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text() = 'Публичный']"))).click()

    # Сохранить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Сохранить']"))).click()
    sleep(0.2)
    print(f"Зона '{name_zone_publ}' создана")

    # Получаю текст уведомление
    browser.implicitly_wait(10)
    notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
    if notifications:
        last_notification_text = notifications[-1].text
        print(f"Текст уведомления: {last_notification_text}")

    # проверка наличия созданной карточки
    if search_line(browser, name_zone_publ):
        print()
    else:
        print(f"'{name_zone_publ}' - не найден.")

    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print( f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")
#                pytest.fail()

# Выполнение функции
def test_add_zone_publ(browser):
    add_zone_publ(browser)




