# Замки и ячейки. Создание набора замков, поиск, удаление

from browser_setup import browser
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import zona_2, num_from_2, num_to_2, new_name_lock, name_BU_text, name_CU_text
from selenium.webdriver import Keys
from time import sleep


def scroll_to_element(browser, element):
    # Прокрутка страницы
    browser.execute_script("arguments[0].scrollIntoView(true);", element)
    sleep(0.1)

def add_search_delete_locks(browser):
    wait = WebDriverWait(browser, 20)
    actions = ActionChains(browser)

    # Клик на Справочники
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Справочники']"))).click()

    # Клик на Зоны
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='table-item'])[1]"))).click()

    # Клик на Добавить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class = 'UIbutton']"))).click()

    # Ввести наименование
    name_zone = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[2]")))
    name_zone.send_keys(zona_2)
#    sleep(1)

    # Номера От
    num1 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[3]")))
    num1.send_keys(Keys.CONTROL, "a")
    num1.send_keys(num_from_2)
#    sleep(1)

    # Номера До
    num2 = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[4]")))
    num2.send_keys(Keys.CONTROL, "a")
    num2.send_keys(num_to_2)
#    sleep(1)

    # Режим доступа
    wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id = 'demo-simple-select-helper']"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "//li[text() = 'Приватный']"))).click()

    # Сохранить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Сохранить']"))).click()
    sleep(0.2)
    print(f"Зона '{zona_2}' создана")
#    time.sleep(1)

    # Получаю текст уведомление
    browser.implicitly_wait(10)
    notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
    if notifications:
        last_notification_text = notifications[-1].text
        print(f"Текс уведомления: {last_notification_text}")

    # Клик на Справочники
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Справочники']"))).click()
#    sleep(1)

    # Клик на замки и ячейки
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class= 'settings-item'])[3]"))).click()
#    sleep(1)

    # Клик на Добавить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class = 'UIbutton']"))).click()
#    sleep(1)

    # Стартовый номер
    start_num = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[3]")))
    start_num.send_keys(Keys.CONTROL, "a")
    start_num.send_keys(num_from_2)

    # Конечный номер
    stop_num = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[4]")))
    stop_num.send_keys(Keys.CONTROL, "a")
    stop_num.send_keys(num_to_2)
#    sleep(1)

    # Колво ячеек
    #count_num = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[5]")))
    #count_num.send_keys(Keys.CONTROL, "a")
    #count_num.send_keys(new_count_lock)
#    sleep(1)

    # Выбрать BU плату
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@id = 'demo-simple-select-helper'])[2]"))).click()
    b = wait.until(EC.element_to_be_clickable((By.XPATH, f"//li[contains(text(), '{name_BU_text}')]")))
    browser.execute_script("arguments[0].scrollIntoView(true);", b)
    browser.execute_script("arguments[0].click();", b)
#    sleep(1)

    # Выбрать CU плату
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@id = 'demo-simple-select-helper'])[3]"))).click()
    c = wait.until(EC.element_to_be_clickable((By.XPATH, f"//li[contains(text(), '{name_CU_text}')]")))
    browser.execute_script("arguments[0].scrollIntoView(true);", c)
    browser.execute_script("arguments[0].click();", c)
#    sleep(1)

    # Стартовый номер на плате
    start_num = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[7]")))
    start_num.send_keys(Keys.CONTROL, "a")
    start_num.send_keys(str(int(num_from_2)-1))
#    sleep(1)

    # Конечный номер на плате
    stop_num = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[8]")))
    stop_num.send_keys(Keys.CONTROL, "a")
    stop_num.send_keys(str(int(num_to_2)-1))
#    sleep(1)

    # Колво плате
    #count_num = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[9]")))
    #count_num.send_keys(Keys.CONTROL, "a")
    #count_num.send_keys(new_count_lock_plata)
#    sleep(1)

    # Выбрать зону
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@id = 'demo-simple-select-helper'])[1]"))).click()
    x = wait.until(EC.element_to_be_clickable((By.XPATH, f"//li[contains(text(), '{zona_2} [{num_from_2}-{num_to_2}]')]")))
    browser.execute_script("arguments[0].scrollIntoView(true);", x)
    x.click()
#    sleep(1)

    # Ввести наименование
    name_lock = wait.until(EC.element_to_be_clickable((By.XPATH, "(//input[@id = 'outlined-basic'])[2]")))
    name_lock.send_keys(new_name_lock)
#    sleep(1)

    # Сохранить
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Сохранить']"))).click()
    sleep(0.2)
    print(f"Набор '{new_name_lock}' создан")

    # Получаю текст уведомление
    browser.implicitly_wait(10)
    notifications = browser.find_elements(By.CLASS_NAME, 'notistack-Snackbar')
    if notifications:
        last_notification_text = notifications[-1].text
        print(f"Текс уведомления: {last_notification_text}")

    # строка поиска
    searc = wait.until(EC.element_to_be_clickable((By.XPATH, "// input[@id = 'outlined-basic']")))
    searc.send_keys(new_name_lock)
    print(f"Искомое значение '{new_name_lock}'")
    sleep(1)

    # поиск
    WebDriverWait(browser, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))
    rows = browser.find_elements(By.CSS_SELECTOR, "tbody tr")
    for row in rows:
        h2_element = row.find_element(By.CSS_SELECTOR, "td:nth-child(1) h2")
        h2_text = h2_element.text.strip()

        if h2_text == new_name_lock:
            print(f"'{h2_text}' найден")
            actions.send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()
            sleep(0.3)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='MuiBox-root css-0']"))).click()
            print(f"'{new_name_lock}' - удален")
            return True
        else:
            print(f"Значение не найдено")
            actions.send_keys(Keys.ESCAPE).send_keys(Keys.ESCAPE).perform()
            sleep(0.1)

    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")
 #               pytest.fail()

def test_add_search_delete_locks(browser):
    add_search_delete_locks(browser)