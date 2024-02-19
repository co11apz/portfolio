""" Импортирование библиотеки для настройки браузера """
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def driver():
    """ Эта функция отвечает за запуск и настройку браузера """

    options = Options()
    options.add_argument("--headless") #Установка опции для запуска браузера без отображения интерфейса.
    options.add_argument("--disable-gpu") #Отключение использования GPU браузером.
    options.add_argument('log-level=3') #Установка уровня логирования на уровень 3 (минимальный уровень)
    options.add_argument("--disable-notifications") #Отключение уведомлений в браузере.
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.accept_untrusted_certs = True
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
