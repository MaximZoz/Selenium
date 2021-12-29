import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

try:

    # ищем элементы в браузере
    input1 = browser.find_element(By.XPATH, "//input[@placeholder='Enter first name']")
    input2 = browser.find_element(By.XPATH, "//input[@placeholder='Enter last name']")

    input3 = browser.find_element(By.XPATH, "//input[@placeholder='Enter email']")

    button = browser.find_element(By.XPATH, "//button[@type='submit' and text()='Submit']")
    file = browser.find_element(By.ID, "file")

    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    # заполняем обязательные поля
    input1.send_keys("Ivan")
    input2.send_keys("Petrov")
    input3.send_keys("Ivan123@gmail.com")

    # прикрепляем файл к форме
    file.send_keys(file_path)

    # отправляем заполненную форму с файлом
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
