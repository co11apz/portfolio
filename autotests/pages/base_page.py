""" Импорт нужных библиотек для написания методов """
import time
import allure
import requests
from selenium.common import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: WebDriver):
        """ Эта функция присваивает атрибуту значение driver """

        self.driver = driver

    def check_button_text(self, locator, expected_value):
        """ Эта функция проверяет текст кнопки """

        actual_value = self.driver.find_element(*locator).text
        if actual_value == expected_value:
            pass
        else:
            raise ValueError(f"тексты кнопок не совпадают actual:{actual_value}, expected:{expected_value}")

    def check_placeholder(self, locator,  expected_value):
        """ Эта функция проверяет значение атрибута placeholder """

        actual_value = self.driver.find_element(*locator).get_attribute("placeholder")
        if actual_value == expected_value:
            pass
        else:
            raise ValueError(f"placeholder'ы не совпадают actual:{actual_value}, expected:{expected_value}")

    def check_headers_yt(self, url, headers, payload):
        """ Эта функция проверяет значения атрибутов headers """

        with allure.step('Проверка скорости ответа сервера'):
            start_time = time.time()
            response = requests.request("POST", url, headers=headers, data=payload)
            end_time = time.time()
            final_time = end_time - start_time
            assert final_time < 2

        with allure.step("API Проверка статус кода"):
            assert response.status_code == 200

        with allure.step("API Проверка значения параметра Content-Type"):
            assert response.headers['Content-Type'] == 'application/json; charset=UTF-8'

        with allure.step("API Проверка значения параметра Server"):
            assert response.headers['Server'] == 'scaffolding on HTTPServer2'

        with allure.step("API Проверка значения параметра Cache-Control"):
            assert response.headers['Cache-Control'] == 'private'

        with allure.step("API Проверка значения параметра X-XSS-Protection"):
            assert response.headers['X-XSS-Protection'] == '0'

        with allure.step("API Проверка значения параметра X-Frame-Options"):
            assert response.headers['X-Frame-Options'] == 'SAMEORIGIN'

        with allure.step("API Проверка значения параметра X-Content-Type-Options"):
            assert response.headers['X-Content-Type-Options'] == 'nosniff'

    def wait_for_page_to_load(self, driver, timeout=10):
        """ Эта функция создает ожидание для загрузки элементов страницы """

        WebDriverWait(driver, timeout).until(
            EC.presence_of_all_elements_located((By.XPATH, "//*"))
        )

    def wait_for_element_visibility(self, locator):
        """ Эта функция создает ожидание для появления элемента """

        try:
            return WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            return False

    def wait_for_element_clickable_web(self, element: WebElement, timeout=20):
        """Ожидает, пока найденный веб-элемент не станет видимым и кликабельным, и кликает по нему."""
        end_time = time.time() + timeout
        while True:
            try:
                if element.is_displayed() and element.is_enabled():
                    element.click()
                    return True
            except Exception as e:
                pass
            time.sleep(0.5)
            if time.time() > end_time:
                break
        raise TimeoutException(f"Элемент не стал видимым и кликабельным после {timeout} секунд")

    def find_and_click_element(self, locator):
        """ Эта функция находит элемент и нажимает на него """

        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        element.click()

    def find_and_click_element_fast(self, locator):
        """ Эта функция находит элемент и нажимает на него (ждет гораздо меньше чем стандартный метод) """

        element = WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(locator))
        element.click()

    def check_elements_click(self, arg):
        """ Эта функция перебирает список элементов, проверяет наличие и кликает на каждый из них """

        elements = arg
        for element in elements:
            time.sleep(1)
            if self.driver.find_element(*element).is_displayed():
                time.sleep(1)
                self.driver.find_element(*element).click()
