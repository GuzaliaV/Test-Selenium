# Права доступа. Добавить пользователя. User_5

from browser_setup import browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from termcolor import cprint
from conftest import lastname6, name6, login6, password6
from time import sleep

def user_6(browser):
    wait = WebDriverWait(browser, 10)

    cprint("Права доступа. Добавить пользователя. User_5 / test_func_add_user_5", "yellow")

    # клик по кнопке Настройки
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[text() = 'Настройки'])[1]"))).click()

    # Права доступа
    wait.until(EC.element_to_be_clickable((By.XPATH, "//h2[text() = 'Права доступа']"))).click()

    # Добавить пользователя
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Добавить пользователя']"))).click()

    # Заполнить поля Фамилия, Имя, Логин, Пароль, Подтверждение пароля

    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'Фамилия*']"))).send_keys(lastname6)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'Имя*']"))).send_keys(name6)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'Логин*']"))).send_keys(login6)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'Пароль*']"))).send_keys(password6)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'Подтверждение пароля*']"))).send_keys(password6)

    # Вкладка Права доступа
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Права доступа']"))).click()

    # Админ - нет
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id = 'Администратор']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text() = 'Нет']"))).click()

    # Открытие ячейки
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id = 'Открытие ячейки']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text() = 'Есть']"))).click()

    print(f"Создан пользователь '{login6}' с паролем '{password6}' с правами доступа: Открытие ячейки.")

    # Сохранить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Сохранить']"))).click()
    sleep(1)

def test_user_6(browser):
    user_6(browser)