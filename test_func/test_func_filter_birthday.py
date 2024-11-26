# Клиенты. Фильтр по дате рождения

from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from datetime import datetime, timedelta
from time import sleep
import random


def generate_random_birthday_range():
    start_date = datetime.strptime("01.01.1950", '%d.%m.%Y')
    end_date = datetime.strptime("12.12.2020", '%d.%m.%Y')

    # Генерируем случайную дату в диапазоне
    random_birth_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

    # Делаем диапазон не более 3 лет
    date_range_start = random_birth_date
    date_range_end = random_birth_date + timedelta(days=3 * 365)  # 3 года

    return date_range_start, date_range_end


def filter_birthday(browser):
    wait = WebDriverWait(browser, 10)

    # Клик по кнопке Клиенты
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()= 'Клиенты']"))).click()
    sleep(0.2)

    # Генерация случайного диапазона дат рождения
    random_start, random_end = generate_random_birthday_range()

    # Форматирование дат
    start_date = random_start.strftime('%d.%m.%Y')
    end_date = random_end.strftime('%d.%m.%Y')

    # Клик по фильтру
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='filter-button']"))).click()

    # Клик на Дата рождения
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()= 'Дата рождения']"))).click()

    # Ввести стартовую дату рождения
    start_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder= 'DD.MM.YYYY']")))
    start_input.click()
    start_input.send_keys(start_date)

    # Ввести конечную дату рождения
    stop_input = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder= 'DD.MM.YYYY'])[2]")))
    stop_input.click()
    stop_input.send_keys(end_date)

    # Применить фильтр
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Применить']"))).click()

    print(f"Фильтр установлен на диапазон: {start_date} - {end_date}")

    # Проверка отфильтрованных клиентов
    filtered_birthdays = []
    rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))
    for row in rows:
        try:
            h2_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(5) h2")
            h2_text = h2_element.text

            if h2_text and h2_text.lower() != 'не указана':
                filtered_birthdays.append(h2_text)
        except Exception as e:
            print(f"Ошибка при получении даты рождения: {e}")

    if filtered_birthdays:
        if all(is_date_in_range(b, start_date, end_date) for b in filtered_birthdays):
            print("Найденные клиенты имеют даты рождения в заданном диапазоне")
        else:
            print("Некоторые отфильтрованные клиенты имеют даты рождения вне заданного диапазона")
    else:
        print("Нет клиентов в данном диапазоне дат рождения")

    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")

    # клик по фильтру
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class = 'filter-button']"))).click()
    # сброс фильтра
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()= 'Сбросить']"))).click()


def is_date_in_range(date_str, start_date, end_date):
    date = datetime.strptime(date_str, '%d.%m.%Y')
    start = datetime.strptime(start_date, '%d.%m.%Y')
    end = datetime.strptime(end_date, '%d.%m.%Y')
    return start <= date <= end


def test_filter_birthday(browser):
    filter_birthday(browser)
