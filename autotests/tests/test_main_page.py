"""Импорт нужных библиотек для запуска тестов"""
import pytest
from autotests.pages.main_page import MainPage
import allure
from autotests.conftest import driver


@pytest.mark.presentation
@allure.suite("API")
@allure.title("API проверка гиперссылок")
def test_api(driver):
    """Запуск тестов для API проверки гиперссылок на главной странице"""

    main_page = MainPage(driver)
    main_page.open_page_api()
    main_page.check_header_logo_button_api()
    main_page.check_left_menu_main_button_api()
    main_page.check_left_menu_subscriptions_button_api()
    main_page.check_left_menu_you_button_api()
    main_page.check_left_menu_history_button_api()
    main_page.check_left_menu_trend_button_api()
    main_page.check_left_menu_music_button_api()
    main_page.check_left_menu_video_games_button_api()
    main_page.check_left_menu_sport_button_api()
    main_page.check_left_menu_catalogue_button_api()
    main_page.check_left_menu_premium_button_api()
    main_page.check_left_menu_yt_music_button_api()
    main_page.check_left_menu_yt_kids_button_api()
    main_page.check_left_menu_reports_button_api()
    main_page.check_closed_left_menu_main_button_api()
    main_page.check_closed_left_menu_subscriptions_button_api()
    main_page.check_closed_left_menu_you_button_api()
    main_page.check_closed_left_menu_history_button_api()


@pytest.mark.presentation
@allure.suite("Header")
@allure.title("Проверка наличия элементов хедэра")
def test_header_items(driver):
    """Запуск тестов для проверки наличия элементов хедэра на главной странице"""

    main_page = MainPage(driver)
    main_page.open_page()
    main_page.check_header_burger_button()
    main_page.check_header_logo_button()
    main_page.check_header_search_field()
    main_page.check_header_keyboard_button()
    main_page.check_header_search_button()
    main_page.check_header_voice_search_button()
    main_page.check_header_options_button()
    main_page.check_header_login_button()


@pytest.mark.presentation
@allure.suite("Settings menu")
@allure.title("Проверка наличия элементов меню настроек")
def test_header_settings_menu_items(driver):
    """Запуск тестов для проверки наличия элементов меню настроек"""

    main_page = MainPage(driver)
    main_page.open_page()
    main_page.open_settings_menu()
    main_page.check_settings_menu_your_data_button()
    main_page.check_settings_menu_theme_button()
    main_page.check_settings_menu_language_button()
    main_page.check_settings_menu_safemode_button()
    main_page.check_settings_menu_country_button()
    main_page.check_settings_menu_hotkeys_button()
    main_page.check_settings_menu_settings_buttton()
    main_page.check_settings_menu_about_button()
    main_page.check_settings_menu_send_report_button()


@pytest.mark.presentation
@allure.suite("Left menu")
@allure.title("Проверка наличия элементов бокового меню")
def test_left_menu_items(driver):
    """Запуск тестов для проверки наличия элементов бокового меню"""

    main_page = MainPage(driver)
    main_page.open_page()
    main_page.check_left_menu_main_button()
    main_page.check_left_menu_shorts_button()
    main_page.check_left_menu_subscriptions_button()
    main_page.check_left_menu_you_button()
    main_page.check_left_menu_history_button()
    main_page.check_left_menu_login_button()
    main_page.check_left_menu_trend_button()
    main_page.check_left_menu_music_button()
    main_page.check_left_menu_video_games_button()
    main_page.check_left_menu_sport_button()
    main_page.check_left_menu_catalogue_button()
    main_page.check_left_menu_premium_button()
    main_page.check_left_menu_yt_music_button()
    main_page.check_left_menu_yt_kids_button()
    main_page.check_left_menu_settings_button()
    main_page.check_left_menu_reports_button()
    main_page.check_left_menu_about_button()
    main_page.check_left_menu_send_report_button()


@pytest.mark.presentation
@allure.suite("Left menu closed")
@allure.title("Проверка наличия элементов закрытого бокового меню")
def test_closed_left_menu_items(driver):
    """Запуск тестов для проверки наличия элементов закрытого бокового меню"""

    main_page = MainPage(driver)
    main_page.open_page()
    main_page.close_left_menu()
    main_page.check_closed_left_menu_main_button()
    main_page.check_closed_left_menu_shorts_button()
    main_page.check_closed_left_menu_subscriptions_button()
    main_page.check_closed_left_menu_you_button()
    main_page.check_closed_left_menu_history_button()


@pytest.mark.presentation
@allure.suite("Categories")
@allure.title("Проверка наличия категорий")
def test_categories(driver):
    """Запуск тестов для проверки наличия категорий"""

    main_page = MainPage(driver)
    main_page.open_page()
    main_page.check_categories()


@pytest.mark.presentation
@allure.suite("Videos")
@allure.title("Проверка видео")
def test_videos(driver):
    """Запуск тестов для проверки видео"""

    main_page = MainPage(driver)
    main_page.open_page()
    main_page.check_videos_img()
    main_page.check_videos()
