# Права доступа. Добавить пользователя. User_4

from browser_setup import browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from termcolor import cprint
from conftest import lastname4, name4, login4, password4
from time import sleep


def user_4(browser):
    wait = WebDriverWait(browser, 10)

    cprint("Права доступа. Добавить пользователя. User_4 / test_func_add_user_4", "yellow")

    # клик по кнопке Настройки
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[text() = 'Настройки'])[1]"))).click()

    # Права доступа
    wait.until(EC.element_to_be_clickable((By.XPATH, "//h2[text() = 'Права доступа']"))).click()

    # Добавить пользователя
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Добавить пользователя']"))).click()

    # Заполнить поля Фамилия, Имя, Логин, Пароль, Подтверждение пароля

    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'Фамилия*']"))).send_keys(lastname4)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'Имя*']"))).send_keys(name4)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'Логин*']"))).send_keys(login4)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'Пароль*']"))).send_keys(password4)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'Подтверждение пароля*']"))).send_keys(password4)

    # Вкладка Права доступа
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Права доступа']"))).click()

    # Админ - нет
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id = 'Администратор']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text() = 'Нет']"))).click()

    # Аренда. Чтение
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id = 'Аренда']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text() = 'Чтение']"))).click()

    print(f"Создан пользователь '{login4}' с паролем '{password4}' с правами доступа: Аренда. Чтение.")

    # Сохранить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Сохранить']"))).click()
    sleep(1)

def test_user_4(browser):
    user_4(browser)