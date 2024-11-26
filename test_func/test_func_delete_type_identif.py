# Типы идентификатора. Создание и удалиение ТИ

from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

def scroll_to_element(browser, element):
    # Прокрутка страницы
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
    sleep(0.1)

def delete_type_ident(browser):
    wait = WebDriverWait(browser, 20)

    type_ident = "ТИ удалить"

    # Клик на Справочники
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Справочники']"))).click()

    # Клик по идентиф
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='table-item'])[4]"))).click()
 #   sleep(0.1)

    # Клик по кнопке Добавить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Добавить']"))).click()

    # Ввести наименование
    name = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[2]")))
    name.send_keys(type_ident)

    # Сохранить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Сохранить']"))).click()
#    sleep(0.2)
    print(f"Создан тип идентификатора со значением '{type_ident}'")

    # Получаю текст уведомление
    browser.implicitly_wait(10)
    notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
    if notifications:
        last_notification_text = notifications[-1].text
        print(f"Текст уведомления: {last_notification_text}")

    found = False
    while not found:
        rows = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))

        for row in rows:
            h2_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(1) h2")
            h2_text = h2_element.text

            # Прокрутка к элементу
            scroll_to_element(browser, h2_element)

            if h2_text == type_ident:
                found = True
                # открыть карточку
                h2_element.click()

                # редактировать
                wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Редактировать']"))).click()

                # Удалить
                wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Удалить']"))).click()
                sleep(1)

                # Получаю текст уведомления
                notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
                if notifications:
                    last_notification_text = notifications[-1].text
                    print(f"Текст уведомления: {last_notification_text}")

                text_1 = "Чтобы удалить тип идентификатора, который принимал участие в операциях - необходимо использовать флаг force=true"
                text_message = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id= 'notistack-snackbar']")))
                text_message_txt = text_message.text

                if text_1.strip() == text_message_txt.strip():
                    wait.until(EC.element_to_be_clickable((By.XPATH, "(//button[text()='Удалить'])[2]"))).click()
                    sleep(0.1)

                # Проверка, что карточка удалена
                rows_after_delete = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))
                if not any(type_ident in row.text for row in rows_after_delete):
                    print(f"'{type_ident}' - удалена")
                else:
                    print(f"'{type_ident}' - не удалена")
                break

        # Перейти на следующую страницу, если карточка не была найдена
        if not found:
            try:
                next_page = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label = 'Go to next page']")))
                next_page.click()
                sleep(0.2)
            except Exception:
                print("Не найден на всех страницах")
                return False

    # Блок для проверки запросов
    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")
                # pytest.fail()

def test_delete_type_ident(browser):
    delete_type_ident(browser)
