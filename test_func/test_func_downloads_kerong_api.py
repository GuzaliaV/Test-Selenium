# загрузка файла на странице kerong api

import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from browser_setup import browser

def downloads_kerong(browser):
    wait = WebDriverWait(browser, 20)

    # клик на настройки
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Настройки']"))).click()

    # клик по разделу kerong api
    wait.until(EC.element_to_be_clickable((By.XPATH, "(//div[@class  = 'settings-item'])[2]"))).click()

    # клик на принтер
    browser.find_element(By.CLASS_NAME, "printer-button").click()
    time.sleep(10)

    for request in browser.requests:
        if request.response:
            if request.response.status_code not in {200, 101}:
                error_message = request.response.body.decode('utf-8')
                print(
                    f"Ошибка на URL: {request.url} с кодом: {request.response.status_code} Текст ошибки: {error_message}")
                pytest.fail()


def test_downloads_kerong(browser):
    downloads_kerong(browser)