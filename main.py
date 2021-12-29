import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/selects1.html"
browser.get(link)


def calc_sum(str_num1, str_num2):
    return str((int(str_num1) + int(str_num2)))


try:
    # получаем числа из span
    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text

    # складываем числа
    res = calc_sum(num1, num2)

    # выбираем мз выпадающего списка это число
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(res)

    # кликаем на submit
    button = browser.find_element(By.TAG_NAME, "[type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
