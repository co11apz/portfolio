""" Импорт нужных библиотек для написания тестов """
import time
import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from autotests.pages.base_page import BasePage
from autotests.pages.locators import main_page_locators
from autotests.pages.api_data import main_page_api_data


class MainPage(BasePage):

    def __init__(self, driver):
        """ Инициализация класса MainPage """

        super().__init__(driver)
        self.driver = driver

#открытие сайта

    def open_page(self):
        """Открывает главную страницу веб-сайта и ожидает её загрузки."""

        with allure.step("Проверка перехода на главную страницу"):
            self.driver.get('https://www.youtube.com/')
            self.wait_for_page_to_load(self.driver)

    def open_page_api(self):
        """Выполняет API-проверку загрузки главной страницы."""

        with allure.step("API проверка загрузки главной страницы"):
            url, payload, headers = main_page_api_data.open_page_api()
            self.check_headers_yt(url, headers, payload)

#проверка наличия кнопок хэдэра

    def check_header_burger_button(self):
        """Проверяет наличие кнопки 'бургер' в хедере."""

        with allure.step("Проверка наличия 'бургер' кнопки"):
            self.find_and_click_element(main_page_locators.burger_button)
            time.sleep(0.2)

    def check_header_logo_button(self):
        """Проверяет наличие кнопки логотипа в хедере."""

        with allure.step("Проверка наличия логотипа"):
            self.find_and_click_element(main_page_locators.logo_button)
            time.sleep(0.2)

    def check_header_logo_button_api(self):
        """Выполняет API-проверку загрузки главной страницы после нажатия на кнопку логотипа."""

        with allure.step("API проверка загрузки гл страницы после нажатия на лого"):
            url, payload, headers = main_page_api_data.check_header_logo_button_api()
            self.check_headers_yt(url, headers, payload)

    def check_header_search_field(self):
        """Проверяет наличие поля поиска и проверяет его параметр placeholder."""

        with allure.step("Проверка наличия поля ввода"):
            self.find_and_click_element(main_page_locators.search_field)
            time.sleep(0.2)

        with allure.step("Проверка параметра placeholder"):
            self.check_placeholder(main_page_locators.placeholder_search_field, 'Введите запрос')

    def check_header_keyboard_button(self):
        """Проверяет наличие кнопки клавиатуры в хедере."""

        with allure.step("Проверка наличия кнопки клавиатуры"):
            self.find_and_click_element(main_page_locators.keyboard_button)
            time.sleep(0.2)

    def check_header_search_button(self):
        """Проверяет наличие кнопки поиска в хедере."""

        with allure.step("Проверка наличия кнопки поиска"):
            self.find_and_click_element(main_page_locators.search_button)
            time.sleep(0.2)

    def check_header_voice_search_button(self):
        """Проверяет наличие кнопки голосового поиска в хедере и отменяет действие."""

        with allure.step("Проверка наличия кнопки голосового поиска"):
            self.find_and_click_element(main_page_locators.voice_search_button)
            time.sleep(0.2)
            self.find_and_click_element(main_page_locators.dop_cancel_button)
            time.sleep(0.2)

    def check_header_options_button(self):
        """Проверяет наличие кнопки настроек в хедере."""

        with allure.step("Проверка наличия кнопки настроек"):
            self.find_and_click_element(main_page_locators.options_button)
            time.sleep(0.2)

    def check_header_login_button(self):
        """Проверяет текст и наличие кнопки входа в хедере."""

        with allure.step("Проверка текста кнопки войти"):
            self.check_button_text(main_page_locators.text_header_login_button, 'Войти')

        with allure.step("Проверка наличия кнопки войти"):
            self.find_and_click_element(main_page_locators.header_login_button)
            time.sleep(0.2)

#проверка наличия кнопок меню настроек

    def open_settings_menu(self):
        """Открывает меню настроек."""

        with allure.step("Открытие меню настроек"):
            self.find_and_click_element(main_page_locators.options_button)

    def check_settings_menu_your_data_button(self):
        """Проверяет наличие кнопки 'Ваши данные' в меню настроек."""

        with allure.step("Проверка наличия кнопки ваши данные"):
            self.find_and_click_element(main_page_locators.your_data_button)
            self.open_page()
            self.open_settings_menu()
            time.sleep(0.5)

    def check_settings_menu_theme_button(self):
        """Проверяет наличие кнопки 'Тема' в меню настроек."""

        with allure.step("Проверка наличия кнопки тема"):
            self.find_and_click_element(main_page_locators.theme_button)
            self.find_and_click_element(main_page_locators.back_button)
            time.sleep(0.5)

    def check_settings_menu_language_button(self):
        """Проверяет наличие кнопки 'Язык' в меню настроек."""

        with allure.step("Проверка наличия кнопки язык"):
            self.find_and_click_element(main_page_locators.language_button)
            self.find_and_click_element(main_page_locators.back_button)
            time.sleep(0.5)

    def check_settings_menu_safemode_button(self):
        """Проверяет наличие кнопки 'Безопасный режим' в меню настроек."""

        with allure.step("Проверка наличия кнопки безопасного режима"):
            self.find_and_click_element(main_page_locators.safemode_button)
            self.find_and_click_element(main_page_locators.back_button)
            time.sleep(0.5)

    def check_settings_menu_country_button(self):
        """Проверяет наличие кнопки 'Выбор страны' в меню настроек."""

        with allure.step("Проверка наличия кнопки выбора страны"):
            self.find_and_click_element(main_page_locators.country_button)
            self.find_and_click_element(main_page_locators.back_button)
            time.sleep(0.5)

    def check_settings_menu_hotkeys_button(self):
        """Проверяет наличие кнопки 'Быстрые клавиши' в меню настроек."""

        with allure.step("Проверка наличия кнопки быстрые клавиши"):
            self.find_and_click_element(main_page_locators.hotkeys_button)
            self.find_and_click_element(main_page_locators.close_button)
            self.find_and_click_element(main_page_locators.options_button)
            time.sleep(0.5)

    def check_settings_menu_settings_buttton(self):
        """Проверяет наличие кнопки 'Настройки' в меню настроек."""

        with allure.step("Проверка наличия кнопки настроек в меню настройки"):
            self.find_and_click_element(main_page_locators.inoptions_button)
            time.sleep(0.5)
            self.open_page()
            self.open_settings_menu()
            time.sleep(0.5)

    def check_settings_menu_about_button(self):
        """Проверяет наличие кнопки 'Справка' в меню настроек."""

        with allure.step("Проверка наличия кнопки справка в меню настройки"):
            self.find_and_click_element(main_page_locators.inabout_button)
            self.driver.implicitly_wait(5)
            iframe = self.wait_for_element_visibility(main_page_locators.iframe_help_main)
            time.sleep(1.1)
            self.driver.switch_to.frame(iframe)
            time.sleep(1)
            iframe = self.wait_for_element_visibility(main_page_locators.iframe_help)
            time.sleep(1)
            self.driver.switch_to.frame(iframe)
            self.find_and_click_element(main_page_locators.report_close_button)
            self.driver.switch_to.default_content()
            time.sleep(0.5)

    def check_settings_menu_send_report_button(self):
        """Проверяет наличие кнопки 'Отправить отзыв' в меню настроек и закрывает соответствующее всплывающее окно."""

        with allure.step("Проверка наличия кнопки отправить отзыв в меню настройки"):
            self.find_and_click_element(main_page_locators.insend_report_button)
            self.driver.implicitly_wait(5)
            iframe = self.wait_for_element_visibility(main_page_locators.iframe_main)
            time.sleep(1)
            self.driver.switch_to.frame(iframe)
            time.sleep(1)
            iframe = self.wait_for_element_visibility(main_page_locators.iframe_feedback)
            time.sleep(1)
            self.driver.switch_to.frame(iframe)
            self.find_and_click_element(main_page_locators.submit_report_close_button)

#проверка наличия кнопок бокового меню

    def check_left_menu_main_button(self):
        """Проверяет наличие кнопки 'Главная' в боковом меню."""

        with allure.step("Проверка наличия кнопки Главная"):
            self.find_and_click_element(main_page_locators.main_button)
            time.sleep(0.5)

    def check_left_menu_main_button_api(self):
        """API Проверка ответа после нажатия на кнопку 'Главная' в боковом меню."""

        with allure.step("API Проверка ответа после нажатия на кнопку Главная"):
            url, payload, headers = main_page_api_data.check_left_menu_main_button_api()
            self.check_headers_yt(url, headers, payload)

    def check_left_menu_shorts_button(self):
        """Проверяет наличие кнопки 'Shorts' в боковом меню."""

        with allure.step("Проверка наличия кнопки Shorts"):
            self.find_and_click_element(main_page_locators.shorts_button)
            time.sleep(0.5)

    def check_left_menu_subscriptions_button(self):
        """Проверяет наличие кнопки 'Подписки' в боковом меню."""

        with allure.step("Проверка наличия кнопки Подписки"):
            self.find_and_click_element(main_page_locators.subscriptions_button)
            time.sleep(0.5)

    def check_left_menu_subscriptions_button_api(self):
        """API проверка ответа после нажатия на кнопку 'Подписки' в боковом меню."""

        with allure.step("API проверка ответа после нажатия на кнопку Подписки"):
            url, payload, headers = main_page_api_data.check_left_menu_subscriptions_button_api()
            self.check_headers_yt(url, headers, payload)

    def check_left_menu_you_button(self):
        """Проверяет наличие кнопки 'Вы' в боковом меню."""

        with allure.step("Проверка наличия кнопки Вы"):
            self.find_and_click_element(main_page_locators.you_button)
            time.sleep(0.5)

    def check_left_menu_you_button_api(self):
        """API проверка ответа после нажатия на кнопку 'Вы' в боковом меню."""

        with allure.step("API проверка ответа после нажатия на кнопку Вы"):
            url, payload, headers = main_page_api_data.check_left_menu_you_button_api()
            self.check_headers_yt(url, headers, payload)

    def check_left_menu_history_button(self):
        """Проверяет наличие кнопки 'История' в боковом меню."""

        with allure.step("Проверка наличия кнопки История"):
            self.find_and_click_element(main_page_locators.history_button)
            time.sleep(0.5)

    def check_left_menu_history_button_api(self):
        """API проверка ответа после нажатия на кнопку 'История' в боковом меню."""

        with allure.step("API проверка ответа после нажатия на кнопку История"):
            url, payload, headers = main_page_api_data.check_left_menu_history_button()
            self.check_headers_yt(url, headers, payload)

    def check_left_menu_login_button(self):
        """Проверяет наличие кнопки 'Войти' в боковом меню и переходит на главную страницу."""

        with allure.step("Проверка наличия кнопки Войти в боковом меню"):
            self.find_and_click_element(main_page_locators.left_login_button)
            time.sleep(0.5)
            self.open_page()
            time.sleep(0.5)

    def check_left_menu_trend_button(self):
        """Проверяет наличие кнопки 'В тренде' в боковом меню."""

        with allure.step("Проверка наличия кнопки В тренде"):
            self.find_and_click_element(main_page_locators.trend_button)
            time.sleep(0.5)

    def check_left_menu_trend_button_api(self):
        """API проверка ответа после нажатия кнопки 'В тренде' в боковом меню."""

        with allure.step("API проверка ответа после нажатия кнопки В тренде"):
            url, payload, headers = main_page_api_data.check_left_menu_trend_button_api()
            self.check_headers_yt(url, headers, payload)

    def check_left_menu_music_button(self):
        """Проверяет наличие кнопки 'Музыка' в боковом меню."""

        with allure.step("Проверка наличия кнопки Музыка"):
            self.find_and_click_element(main_page_locators.music_button)
            time.sleep(0.5)

    def check_left_menu_music_button_api(self):
        """API проверка ответа после нажатия на кнопку 'Музыка' в боковом меню."""

        with allure.step("API проверка ответа после нажатия на кнопку Музыка"):
            url, payload, headers = main_page_api_data.check_left_menu_music_button_api()
            self.check_headers_yt(url, headers, payload)

    def check_left_menu_video_games_button(self):
        """Проверяет наличие кнопки 'Видеоигры' в боковом меню."""

        with allure.step("Проверка наличия кнопки Видеоигры"):
            self.find_and_click_element(main_page_locators.videogames_button)
            time.sleep(0.5)

    def check_left_menu_video_games_button_api(self):
        """API проверка ответа после нажатия на кнопку 'Видеоигры' в боковом меню."""

        with allure.step("API проверка ответа после нажатия на кнопку Видеоигры"):
            url, payload, headers = main_page_api_data.check_left_menu_video_games_button_api()
            self.check_headers_yt(url, headers, payload)

    def check_left_menu_sport_button(self):
        """Проверяет наличие кнопки 'Спорт' в боковом меню."""

        with allure.step("Проверка наличия кнопки Спорт"):
            self.find_and_click_element(main_page_locators.sport_button)
            time.sleep(0.5)

    def check_left_menu_sport_button_api(self):
        """API проверка ответа после нажатия на кнопку 'Спорт' в боковом меню."""

        with allure.step("API проверка ответа после нажатия на кнопку Спорт"):
            url, payload, headers = main_page_api_data.check_left_menu_sport_button_api()
            self.check_headers_yt(url, headers, payload)

    def check_left_menu_catalogue_button(self):
        """Проверяет наличие кнопки 'Каталог каналов' в боковом меню."""

        with allure.step("Проверка наличия кнопки Каталог каналов"):
            self.find_and_click_element(main_page_locators.catalogue_button)
            time.sleep(0.5)

    def check_left_menu_catalogue_button_api(self):
        """API проверка ответа после нажатия на кнопку 'Каталог каналов' в боковом меню."""

        with allure.step("API проверка ответа после нажатия на кнопку Каталог каналов"):
            url, payload, headers = main_page_api_data.check_left_menu_catalogue_button_api()
            self.check_headers_yt(url, headers, payload)

    def check_left_menu_premium_button(self):
        """Проверяет наличие кнопки 'YouTube Premium' в боковом меню и возвращается на главную страницу."""

        with allure.step("Проверка наличия кнопки YouTube Premium"):
            self.find_and_click_element(main_page_locators.premium_button)
            self.wait_for_page_to_load(self.driver)
            time.sleep(0.5)
            self.find_and_click_element(main_page_locators.burger_button)
            time.sleep(0.5)

    def check_left_menu_premium_button_api(self):
        """API проверка ответа после нажатия на кнопку 'YouTube Premium' в боковом меню."""

        with allure.step("API проверка ответа после нажатия на кнопку YouTube Premium"):
            url, payload, headers = main_page_api_data.check_left_menu_premium_button_api()
            self.check_headers_yt(url, headers, payload)

    def check_left_menu_yt_music_button(self):
        """Проверяет наличие кнопки 'YouTube Music' в боковом меню и закрывает страницу, если открыта."""

        with allure.step("Проверка наличия кнопки YouTube Music"):
            self.find_and_click_element(main_page_locators.yt_music_button)
            self.wait_for_page_to_load(self.driver)
            if self.driver.current_url == 'https://music.youtube.com/':
                self.driver.close()
            time.sleep(0.5)

    def check_left_menu_yt_music_button_api(self):
        """API проверка ответа после нажатия на кнопку 'YouTube Music' в боковом меню."""

        with allure.step("API проверка ответа после нажатия на кнопку YouTube Music"):
            url, payload, headers = main_page_api_data.check_left_menu_yt_music_button_api()
            self.check_headers_yt(url, headers, payload)

    def check_left_menu_yt_kids_button(self):
        """Проверяет наличие кнопки 'YouTube Детям' в боковом меню и закрывает страницу, если открыта."""

        with allure.step("Проверка наличия кнопки YouTube Детям"):
            self.find_and_click_element(main_page_locators.yt_kids_button)
            self.wait_for_page_to_load(self.driver)
            if self.driver.current_url == 'https://www.youtubekids.com/?source=youtube_web':
                self.driver.close()
            time.sleep(0.5)

    def check_left_menu_yt_kids_button_api(self):
        """API проверка ответа после нажатия на кнопку 'YouTube Детям' в боковом меню."""

        with allure.step("API проверка ответа после нажатия на кнопку YouTube Детям"):
            url, payload, headers = main_page_api_data.check_left_menu_yt_kids_button_api()
            self.check_headers_yt(url, headers, payload)

    def check_left_menu_settings_button(self):
        """Проверяет наличие кнопки 'Настройки' в боковом меню и возвращается на главную страницу."""

        with allure.step("Проверка наличия кнопки Настройки в боковом меню"):
            all_handles = self.driver.window_handles
            self.driver.switch_to.window(all_handles[0])
            self.find_and_click_element(main_page_locators.settings_button)
            self.wait_for_page_to_load(self.driver)
            self.driver.get('https://www.youtube.com/')
            time.sleep(0.5)

    def check_left_menu_reports_button(self):
        """Проверяет наличие кнопки 'Жалобы' в боковом меню."""

        with allure.step("Проверка наличия кнопки Жалобы"):
            self.find_and_click_element(main_page_locators.reports_button)
            time.sleep(0.5)

    def check_left_menu_reports_button_api(self):
        """API проверка ответа после нажатия на кнопку 'Жалобы' в боковом меню."""

        with allure.step("API проверка ответа после нажатия на кнопку Жалобы"):
            url, payload, headers = main_page_api_data.check_left_menu_reports_button_api()
            self.check_headers_yt(url, headers, payload)

    def check_left_menu_about_button(self):
        """Проверяет наличие кнопки 'Справка' в боковом меню."""

        with allure.step("Проверка наличия кнопки Справка в боковом меню"):
            self.find_and_click_element(main_page_locators.about_button)
            self.driver.implicitly_wait(5)
            iframe = self.wait_for_element_visibility(main_page_locators.iframe_help_main)
            time.sleep(1.1)
            self.driver.switch_to.frame(iframe)
            time.sleep(1)
            iframe = self.wait_for_element_visibility(main_page_locators.iframe_help)
            time.sleep(1)
            self.driver.switch_to.frame(iframe)
            self.find_and_click_element(main_page_locators.report_close_button)
            self.driver.switch_to.default_content()
            time.sleep(0.5)

    def check_left_menu_send_report_button(self):
        """Проверяет наличие кнопки 'Отправить отзыв' в боковом меню и закрывает всплывающее окно отчета."""

        with allure.step("Проверка наличия кнопки Отправить отзыв"):
            self.find_and_click_element(main_page_locators.send_report_button)
            self.driver.implicitly_wait(5)
            iframe = self.wait_for_element_visibility(main_page_locators.iframe_main)
            time.sleep(1)
            self.driver.switch_to.frame(iframe)
            time.sleep(1)
            iframe = self.wait_for_element_visibility(main_page_locators.iframe_feedback)
            time.sleep(1)
            self.driver.switch_to.frame(iframe)
            self.find_and_click_element(main_page_locators.submit_report_close_button)

#проверка кнопок бокового меню при закрытом меню

    def close_left_menu(self):
        """Закрывает боковое меню."""

        with allure.step("Закрытие бокового меню"):
            self.find_and_click_element(main_page_locators.burger_button)
            time.sleep(0.5)

    def check_closed_left_menu_main_button(self):
        """Проверяет наличие кнопки 'Главная' при закрытом боковом меню."""

        with allure.step("Проверка наличия кнопки Главная при закрытом меню"):
            self.find_and_click_element(main_page_locators.closed_main_button)
            time.sleep(0.2)

    def check_closed_left_menu_main_button_api(self):
        """API проверка ответа после нажатия на кнопку 'Главная' при закрытом боковом меню."""

        with allure.step("API проверка ответа после нажатия на кнопку Главная при закрытом меню"):
            url, payload, headers = main_page_api_data.check_closed_left_menu_main_button_api()
            self.check_headers_yt(url, headers, payload)

    def check_closed_left_menu_shorts_button(self):
        """Проверяет наличие кнопки 'Shorts' при закрытом боковом меню."""

        with allure.step("Проверка наличия кнопки Shorts при закрытом меню"):
            self.find_and_click_element(main_page_locators.closed_shorts_button)
            time.sleep(0.2)

    def check_closed_left_menu_subscriptions_button(self):
        """Проверяет наличие кнопки 'Подписки' при закрытом боковом меню."""

        with allure.step("Проверка наличия кнопки Подписки при закрытом меню"):
            self.find_and_click_element(main_page_locators.closed_subscriptions_button)
            time.sleep(0.2)

    def check_closed_left_menu_subscriptions_button_api(self):
        """API проверка ответа после нажатия на кнопку 'Подписки' при закрытом боковом меню."""

        with allure.step("API проверка ответа после нажатия на кнопку Подписки при закрытом меню"):
            url, payload, headers = main_page_api_data.check_closed_left_menu_subscriptions_button_api()
            self.check_headers_yt(url, headers, payload)

    def check_closed_left_menu_you_button(self):
        """Проверяет наличие кнопки 'Вы' при закрытом боковом меню."""

        with allure.step("Проверка наличия кнопки Вы при закрытом меню"):
            self.find_and_click_element(main_page_locators.closed_you_button)
            time.sleep(0.2)

    def check_closed_left_menu_you_button_api(self):
        """API проверка ответа после нажатия на кнопку 'Вы' при закрытом боковом меню."""

        with allure.step("API проверка ответа после нажатия на кнопку Вы при закрытом меню"):
            url, payload, headers = main_page_api_data.check_closed_left_menu_you_button_api()
            self.check_headers_yt(url, headers, payload)

    def check_closed_left_menu_history_button(self):
        """Проверяет наличие кнопки 'История' при закрытом боковом меню."""

        with allure.step("Проверка наличия кнопки История при закрытом меню"):
            self.find_and_click_element(main_page_locators.closed_history_button)
            time.sleep(0.2)

    def check_closed_left_menu_history_button_api(self):
        """API проверка ответа после нажатия на кнопку 'История' при закрытом боковом меню."""

        with allure.step("API проверка ответа после нажатия на кнопку История при закрытом меню"):
            url, payload, headers = main_page_api_data.check_closed_left_menu_history_button_api()
            self.check_headers_yt(url, headers, payload)

#проверка наличия категорий

    def check_categories(self):
        """Проверяет наличие категорий."""

        with allure.step("Проверка наличия категорий"):
            categories = self.driver.find_elements(By.CSS_SELECTOR, main_page_locators.categories)
            count = 0
            for category in categories:
                try:
                    if count == 4:
                        self.find_and_click_element_fast(main_page_locators.categoria_next)
                        time.sleep(0.5)
                except TimeoutException as e:
                    pass
                finally:
                    self.wait_for_element_clickable_web(category, 20)
                    count += 1
                    time.sleep(2)
#проверка видео

    def check_videos(self):
        """Проверяет наличие видео."""

        with allure.step("Проверка наличия видео"):
            videos = self.driver.find_elements(By.XPATH, main_page_locators.videos)

            for video in videos[0:5]:
                video.click()
                self.wait_for_page_to_load(self.driver)
                self.driver.back()
                time.sleep(0.2)

    def check_videos_img(self):
        """Проверяет наличие превью у видео."""

        with allure.step("Проверка наличия превью у видео"):
            videos_img = self.driver.find_elements(By.XPATH, main_page_locators.videos_img)

            for video_img in videos_img[0:5]:
                video_img.is_displayed()
                time.sleep(0.2)
