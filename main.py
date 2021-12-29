import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)


def calc(str_num):
    return str(math.log(abs(12 * math.sin(int(str_num)))))


try:

    # ищем элементы в браузере

    button = browser.find_element(By.TAG_NAME, "[type='submit']")

    button.click()


    # нажимаем ок на alert
    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element(By.ID, "input_value").text
    answer = browser.find_element(By.ID, "answer")
    y = calc(x_element)
    answer.send_keys(y)

    button = browser.find_element(By.TAG_NAME, "[type='submit']")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
