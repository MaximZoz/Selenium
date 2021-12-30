import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from CustomBrowser import CustomBrowser

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = CustomBrowser()
browser.get(link)

try:
    # дожидаемся 12 секунд когда price будет равен 100
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    # кликаем на кнопку
    button = browser.find_element(By.ID, "book")
    button.click()

    # вводим проверку
    browser.solve_captcha()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
