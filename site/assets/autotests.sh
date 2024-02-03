#!/bin/bash

cd /c/Users/roman/PycharmProjects/portfolio/

# Запуск тестов и сохранение результатов в allure-results
pytest -s -v --alluredir=./autotests/allure-results ./autotests/tests/test_main_page.py

# Генерация отчета Allure
allure generate -o ./autotests/allure-reports ./autotests/allure-results --clean

# Запуск встроенного сервера Allure для просмотра отчета в браузере
allure serve ./autotests/allure-results

