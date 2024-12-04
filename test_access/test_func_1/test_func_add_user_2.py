# Права доступа. Добавить пользователя. User_2

from browser_setup import browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from termcolor import cprint
from conftest import lastname2, name2, login2, password2
from time import sleep


def user_2(browser):
    wait = WebDriverWait(browser, 10)

    cprint("Права доступа. Добавить пользователя. User_2 / test_func_add_user_2", "yellow")

    # клик по кнопке Настройки
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[text() = 'Настройки'])[1]"))).click()

    # Права доступа
    wait.until(EC.element_to_be_clickable((By.XPATH, "//h2[text() = 'Права доступа']"))).click()

    # Добавить пользователя
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Добавить пользователя']"))).click()

    # Заполнить поля Фамилия, Имя, Логин, Пароль, Подтверждение пароля

    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'Фамилия*']"))).send_keys(lastname2)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'Имя*']"))).send_keys(name2)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'Логин*']"))).send_keys(login2)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'Пароль*']"))).send_keys(password2)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'Подтверждение пароля*']"))).send_keys(password2)

    # Вкладка Права доступа
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Права доступа']"))).click()

    # Админ - нет
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id = 'Администратор']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text() = 'Нет']"))).click()

    # Клиенты. Запись/Чтение
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id = 'Клиенты']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text() = 'Запись/чтение']"))).click()

    print(f"Создан пользователь '{login2}' с паролем '{password2}' с правами доступа: Клиенты. Запись/чтение")

    # Сохранить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Сохранить']"))).click()
    sleep(1)

def test_user_2(browser):
    user_2(browser)