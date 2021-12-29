import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"
browser.get(link)


def calc(str_num):
    return str(math.log(abs(12 * math.sin(int(str_num)))))


try:

    # находим число из страницы, подставляем его в формулу
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    # вводим в input то, что получилось
    answer = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(y)

    # отмечаем checkbox "I'm the robot"
    robotCheckbox = browser.find_element(By.ID, "robotCheckbox")
    robotCheckbox.click()

    # выбираем radiobutton "Robots rule!"
    robotsRule = browser.find_element(By.ID, "robotsRule")
    robotsRule.click()

    # кликаем на submit
    button = browser.find_element(By.TAG_NAME, "[type='submit']")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
