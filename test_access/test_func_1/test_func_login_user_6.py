# войти под учеткой user_6

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import servername, port_auth
from browser_setup import browser
from conftest import login6, password6
from time import sleep


def login_user_6(browser):
    wait = WebDriverWait(browser, 10)

    # нажать кнопку "монетки"
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='server-btn']"))).click()

    # найти поле адрес сервера, очистить, ввести адрес сервера
    server = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='Адрес сервера']")))
    server.send_keys(Keys.BACKSPACE * 15)
    server.send_keys(servername)

    # найти поле Порт, очистить, ввести верный порт
    port = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='Порт сервера']")))
    port.send_keys(Keys.BACKSPACE * 4)
    port.send_keys(port_auth)

    # Сохранить данные
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Сохранить данные']"))).click()

    # ввести логин
    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='Логин']"))).send_keys(login6)

    # ввести пароль
    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='Пароль']"))).send_keys(password6)

    # клик по кнопке войти
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class= 'UIbutton']"))).click()
    sleep(1)

    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200,101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")

    print_sections(browser)

def print_sections(browser):
    wait = WebDriverWait(browser, 10)

    # Ждем загрузку бокового меню
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "side-menu-items-container")))

    # Получаем все кнопки-разделы на боковой панели
    sections = browser.find_elements(By.CSS_SELECTOR, ".menu-items, .menu-items-focus")

    print("У пользователя 'user_6' с правами доступа 'Открытие ячейки' доступны разделы:")
    for section in sections:
        print(f"- {section.text}")

def test_login_user_6(browser):
    login_user_6(browser)