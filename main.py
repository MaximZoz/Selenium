import time
import math
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Список ссылок на тестируемые страницы
links = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
]


@pytest.fixture(scope='function')
def answer():
    """
    Фистура применяется к функции теста.
    :return: Возвращает результат формулы math.log(int(time.time()))
    :rtype: str
    """
    return str(math.log(int(time.time())))


class Test_Stepik:

    @classmethod
    def setup_class(cls):
        """
        Метод класса инициализирует вебдрайвер.
        Устанавливает неявное ожидание
        """
        cls.browser = webdriver.Chrome()
        cls.browser.implicitly_wait(5)

    @classmethod
    def teardown_class(cls):
        """
        Метод класса закрывает браузер
        """
        cls.browser.quit()

    @pytest.mark.parametrize('link', links)
    def test_stepik(self, link, answer):
        result = ""
        browser = self.browser
        # Открывает страницу
        browser.get(link)
        # Ожидает появления элемента с тегом "textarea"
        textarea = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea"))
        )
        # Передаем ответ из фикстуры answer в поле ввода
        textarea.send_keys(answer)
        # Нажимаем кнопку
        browser.find_element_by_css_selector('button.submit-submission ').click()
        # Получаем текст элемента, подтверждающего правильность ответа
        feedback = browser.find_element_by_css_selector('pre.smart-hints__hint').text
        # Проверяем ответ
        assert feedback == 'Correct!', f'Error: {feedback}'
