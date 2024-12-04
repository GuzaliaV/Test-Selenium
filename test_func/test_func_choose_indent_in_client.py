# Клиенты. Карточка клиента. Выбрать идентификатор


from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from termcolor import cprint

def choose_indent_in_client(browser):
    actions = ActionChains(browser)
    wait = WebDriverWait(browser, 10)

    cprint("Клиенты. Карточка клиента. Выбрать идентификатор / test_func_choose_indent_in_client", "yellow")

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
            # Получение имени клиента
            client_name_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(1) h4")
            client_name = client_name_element.text if client_name_element else "Имя не указано"

            actions.move_to_element(row).click().perform()

            # Кнопка "Выбрать"
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Выбрать']"))).click()
            sleep(0.1)

            # Клик по идентификатору
            ident = browser.find_element(By.CSS_SELECTOR, "tbody tr:first-child h2")
            print(f"Клиенту '{client_name}' привязан идентификатор '{ident.text}'")
            ident.click()
            sleep(1)

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
        return choose_indent_in_client(browser)
    except:
        return False


def test_choose_indent_in_client(browser):
    choose_indent_in_client(browser)
    return choose_indent_in_client(browser)