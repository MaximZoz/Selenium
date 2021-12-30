import math

from selenium import webdriver
from selenium.webdriver.common.by import By


class CustomBrowser(webdriver.Chrome):

    def solve_captcha(self):
        value_x = int(self.find_element(By.ID, "input_value").text)
        value_x = math.log(abs(12 * math.sin(value_x)))
        self.find_element(By.ID, "answer").send_keys(str(value_x))
        self.find_element(By.TAG_NAME, "[type='submit']").click()
