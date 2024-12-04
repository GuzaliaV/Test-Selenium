# Клиенты. Добавить идентификатор в карточке Клиента

from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from faker import Faker
from termcolor import cprint


def scroll_to_element(browser, element):
    # Прокрутка страницы
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
    sleep(0.1)

def add_ident_in_client(browser):
    actions = ActionChains(browser)
    wait = WebDriverWait(browser, 10)

    cprint("Клиенты. Добавить идентификатор в карточке Клиента / test_func_add_ident_in_client", "yellow")

    # клик по кнопке Клиент
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()= 'Клиенты']"))).click()

    # Поиск клиента у которого не привязан идентификатор
    WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))
    rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")
    for row in rows:
        ident = row.find_element(By.CSS_SELECTOR, "td:nth-child(3) h2")
        ident_text = ident.text

        # открытие клиента и выбор идентифкатора
        if ident_text == '':
            actions.move_to_element(row).click().perform()

            # Кнопка "Добавить"
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Добавить']"))).click()
            sleep(0.1)

            # имя клиента
            name = browser.find_element(By.XPATH, "//input[@id = 'Имя']")
            value = name.get_attribute("value")

            # Выбрать ТИ
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='Выбрать тип идентификатора']"))).click()
            sleep(0.1)
            # Клик по идентификатору
            type = browser.find_element(By.CSS_SELECTOR, "li:nth-child(1)")
            print(f"Выбран ТИ '{type.text}'")
            type.click()

            # ввести значение идентификатора
            ident = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id = 'Значение']")))
            ident.click()
            fake = Faker("ru_RU")
            ident_1 = fake.postcode()
            ident.send_keys(ident_1)
            print(f"Клиенту '{value}' привязан идентификатор '{ident_1}'")

            # сохранить
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Сохранить']"))).click()
            sleep(0.5)

            # Получаю текст уведомление
            browser.implicitly_wait(10)
            notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
            if notifications:
                last_notification_text = notifications[-1].text
                print(f"Текст уведомления: {last_notification_text}")
            break

        for request in browser.requests:
            if request.response:
                if request.response.status_code not in {200, 101}:
                    error_message = request.response.body.decode('utf-8')
                    print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")

    # Если не найден, клик на следующую страницу
    try:
        next_page = browser.find_element(By.XPATH, "//button[@aria-label='Go to next page']")
        next_page.click()
        # рекурсивный вызов функции
        return add_ident_in_client(browser)
    except:
        return False

def test_add_ident_in_client(browser):
    add_ident_in_client(browser)