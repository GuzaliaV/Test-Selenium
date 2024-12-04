# Права доступа. Добавить пользователя. User_3

from browser_setup import browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from termcolor import cprint
from conftest import lastname3, name3, login3, password3
from time import sleep


def user_3(browser):
    wait = WebDriverWait(browser, 10)

    cprint("Права доступа. Добавить пользователя. User_3 / test_func_add_user_3", "yellow")

    # клик по кнопке Настройки
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[text() = 'Настройки'])[1]"))).click()

    # Права доступа
    wait.until(EC.element_to_be_clickable((By.XPATH, "//h2[text() = 'Права доступа']"))).click()

    # Добавить пользователя
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Добавить пользователя']"))).click()

    # Заполнить поля Фамилия, Имя, Логин, Пароль, Подтверждение пароля

    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'Фамилия*']"))).send_keys(lastname3)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'Имя*']"))).send_keys(name3)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'Логин*']"))).send_keys(login3)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'Пароль*']"))).send_keys(password3)

    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'Подтверждение пароля*']"))).send_keys(password3)

    # Вкладка Права доступа
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Права доступа']"))).click()

    # Админ - нет
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id = 'Администратор']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text() = 'Нет']"))).click()

    # Отчеты
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id = 'Отчеты']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text() = 'Есть']"))).click()

    print(f"Создан пользователь '{login3}' с паролем '{password3}' с правами доступа: Отчеты.")

    # Сохранить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Сохранить']"))).click()
    sleep(1)


def test_user_3(browser):
    user_3(browser)