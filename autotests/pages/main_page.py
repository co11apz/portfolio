import time
import allure
from selenium.webdriver.common.by import By
from autotests.pages.base_page import BasePage
from autotests.pages.locators import main_page_locators


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_page(self):
        with allure.step("Проверка перехода на главную страницу"):
            self.driver.get('https://www.youtube.com/')
            self.wait_for_page_to_load(self.driver)

#проверка наличия кнопок хэдэра

    def check_header_burger_button(self):
        with allure.step("Проверка наличия 'бургер' кнопки"):
            self.click_element(main_page_locators.burger_button)
            time.sleep(0.2)

    def check_header_logo_button(self):
        with allure.step("Проверка наличия логотипа"):
            self.click_element(main_page_locators.logo_button)
            time.sleep(0.2)

    def check_header_search_field(self):
        with allure.step("Проверка наличия поля ввода"):
            self.click_element(main_page_locators.search_field)
            time.sleep(0.2)

    def check_header_keyboard_button(self):
        with allure.step("Проверка наличия кнопки клавиатуры"):
            self.click_element(main_page_locators.keyboard_button)
            time.sleep(0.2)

    def check_header_search_button(self):
        with allure.step("Проверка наличия кнопки поиска"):
            self.click_element(main_page_locators.search_button)
            time.sleep(0.2)

    def check_header_voice_search_button(self):
        with allure.step("Проверка наличия кнопки голосового поиска"):
            self.click_element(main_page_locators.voice_search_button)
            time.sleep(0.2)
            self.click_element(main_page_locators.dop_cancel_button)
            time.sleep(0.2)

    def check_header_options_button(self):
        with allure.step("Проверка наличия кнопки настроек"):
            self.click_element(main_page_locators.options_button)
            time.sleep(0.2)

    def check_header_login_button(self):
        with allure.step("Проверка наличия кнопки войти"):
            self.click_element(main_page_locators.header_login_button)
            time.sleep(0.2)

#проверка наличия кнопок меню настроек

    def open_settings_menu(self):
        with allure.step("Открытие меню настроек"):
            self.click_element(main_page_locators.options_button)

    def check_settings_menu_your_data_button(self):
        with allure.step("Проверка наличия кнопки ваши данные"):
            self.click_element(main_page_locators.your_data_button)
            self.open_page()
            self.open_settings_menu()
            time.sleep(0.5)

    def check_settings_menu_theme_button(self):
        with allure.step("Проверка наличия кнопки тема"):
            self.click_element(main_page_locators.theme_button)
            self.click_element(main_page_locators.back_button)
            time.sleep(0.5)

    def check_settings_menu_language_button(self):
        with allure.step("Проверка наличия кнопки язык"):
            self.click_element(main_page_locators.language_button)
            self.click_element(main_page_locators.back_button)
            time.sleep(0.5)

    def check_settings_menu_safemode_button(self):
        with allure.step("Проверка наличия кнопки безопасного режима"):
            self.click_element(main_page_locators.safemode_button)
            self.click_element(main_page_locators.back_button)
            time.sleep(0.5)

    def check_settings_menu_country_button(self):
        with allure.step("Проверка наличия кнопки выбора страны"):
            self.click_element(main_page_locators.country_button)
            self.click_element(main_page_locators.back_button)
            time.sleep(0.5)

    def check_settings_menu_hotkeys_button(self):
        with allure.step("Проверка наличия кнопки быстрые клавиши"):
            self.click_element(main_page_locators.hotkeys_button)
            self.click_element(main_page_locators.close_button)
            self.click_element(main_page_locators.options_button)
            time.sleep(0.5)

    def check_settings_menu_settings_buttton(self):
        with allure.step("Проверка наличия кнопки настроек в меню настройки"):
            self.click_element(main_page_locators.inoptions_button)
            time.sleep(0.5)
            self.open_page()
            self.open_settings_menu()
            time.sleep(0.5)

    def check_settings_menu_about_button(self):
        with allure.step("Проверка наличия кнопки справка в меню настройки"):
            self.wait_for_element_visibility(main_page_locators.inabout_button)
            # self.driver.implicitly_wait(5)
            # iframe = self.wait_for_element_visibility(main_page_locators.iframe_help)
            # self.driver.switch_to.frame(iframe)
            # self.click_element(main_page_locators.report_close_button)
            # time.sleep(0.5)

    def check_settings_menu_send_report_button(self):
        with allure.step("Проверка наличия кнопки отправить отзыв в меню настройки"):
            self.click_element(main_page_locators.insend_report_button)
            self.driver.implicitly_wait(5)
            iframe = self.wait_for_element_visibility(main_page_locators.iframe_feedback)
            self.driver.switch_to.frame(iframe)
            self.click_element(main_page_locators.report_close_button)

#проверка наличия кнопок бокового меню

    def check_left_menu_main_button(self):
        with allure.step("Проверка наличия кнопки Главная"):
            self.click_element(main_page_locators.main_button)
            time.sleep(0.5)

    def check_left_menu_shorts_button(self):
        with allure.step("Проверка наличия кнопки Shorts"):
            self.click_element(main_page_locators.shorts_button)
            time.sleep(0.5)

    def check_left_menu_subscriptions_button(self):
        with allure.step("Проверка наличия кнопки Подписки"):
            self.click_element(main_page_locators.subscriptions_button)
            time.sleep(0.5)

    def check_left_menu_you_button(self):
        with allure.step("Проверка наличия кнопки Вы"):
            self.click_element(main_page_locators.you_button)
            time.sleep(0.5)

    def check_left_menu_history_button(self):
        with allure.step("Проверка наличия кнопки История"):
            self.click_element(main_page_locators.history_button)
            time.sleep(0.5)

    def check_left_menu_login_button(self):
        with allure.step("Проверка наличия кнопки Войти в боковом меню"):
            self.click_element(main_page_locators.left_login_button)
            time.sleep(0.5)
            self.open_page()
            time.sleep(0.5)

    def check_left_menu_trend_button(self):
        with allure.step("Проверка наличия кнопки В тренде"):
            self.click_element(main_page_locators.trend_button)
            time.sleep(0.5)

    def check_left_menu_music_button(self):
        with allure.step("Проверка наличия кнопки Музыка"):
            self.click_element(main_page_locators.music_button)
            time.sleep(0.5)

    def check_left_menu_video_games_button(self):
        with allure.step("Проверка наличия кнопки Видеоигры"):
            self.click_element(main_page_locators.videogames_button)
            time.sleep(0.5)

    def check_left_menu_sport_button(self):
        with allure.step("Проверка наличия кнопки Спорт"):
            self.click_element(main_page_locators.sport_button)
            time.sleep(0.5)

    def check_left_menu_catalogue_button(self):
        with allure.step("Проверка наличия кнопки Каталог каналов"):
            self.click_element(main_page_locators.catalogue_button)
            time.sleep(0.5)

    def check_left_menu_premium_button(self):
        with allure.step("Проверка наличия кнопки YouTube Premium"):
            self.click_element(main_page_locators.premium_button)
            self.wait_for_page_to_load(self.driver)
            time.sleep(0.5)
            self.click_element(main_page_locators.burger_button)
            time.sleep(0.5)

    def check_left_menu_yt_music_button(self):
        with allure.step("Проверка наличия кнопки YouTube Music"):
            self.click_element(main_page_locators.yt_music_button)
            self.wait_for_page_to_load(self.driver)
            if self.driver.current_url == 'https://music.youtube.com/':
                self.driver.close()
            time.sleep(0.5)

    def check_left_menu_yt_kids_button(self):
        with allure.step("Проверка наличия кнопки YouTube Детям"):
            self.click_element(main_page_locators.yt_kids_button)
            self.wait_for_page_to_load(self.driver)
            if self.driver.current_url == 'https://www.youtubekids.com/?source=youtube_web':
                self.driver.close()
            time.sleep(0.5)

    def check_left_menu_settings_button(self):
        with allure.step("Проверка наличия кнопки Настройки в боковом меню"):
            all_handles = self.driver.window_handles
            self.driver.switch_to.window(all_handles[0])
            self.click_element(main_page_locators.settings_button)
            self.wait_for_page_to_load(self.driver)
            self.driver.get('https://www.youtube.com/')
            time.sleep(0.5)

    def check_left_menu_reports_button(self):
        with allure.step("Проверка наличия кнопки Жалобы"):
            self.click_element(main_page_locators.reports_button)
            time.sleep(0.5)

    def check_left_menu_about_button(self):
        with allure.step("Проверка наличия кнопки Справка в боковом меню"):
            self.wait_for_element_visibility(main_page_locators.about_button)
            time.sleep(0.5)

    def check_left_menu_send_report_button(self):
        with allure.step("Проверка наличия кнопки Отправить отзыв"):
            self.click_element(main_page_locators.send_report_button)
            self.driver.implicitly_wait(5)
            iframe = self.wait_for_element_visibility(main_page_locators.iframe_feedback)
            self.driver.switch_to.frame(iframe)
            self.click_element(main_page_locators.report_close_button)

#проверка кнопок бокового меню при закрытом меню

    def close_left_menu(self):
        with allure.step("Закрытие бокового меню"):
            self.click_element(main_page_locators.burger_button)
            time.sleep(0.5)

    def check_closed_left_menu_main_button(self):
        with allure.step("Проверка наличия кнопки Главная при закрытом меню"):
            self.click_element(main_page_locators.closed_main_button)
            time.sleep(0.2)

    def check_closed_left_menu_shorts_button(self):
        with allure.step("Проверка наличия кнопки Shorts при закрытом меню"):
            self.click_element(main_page_locators.closed_shorts_button)
            time.sleep(0.2)

    def check_closed_left_menu_subscriptions_button(self):
        with allure.step("Проверка наличия кнопки Подписки при закрытом меню"):
            self.click_element(main_page_locators.closed_subscriptions_button)
            time.sleep(0.2)

    def check_closed_left_menu_you_button(self):
        with allure.step("Проверка наличия кнопки Вы при закрытом меню"):
            self.click_element(main_page_locators.closed_you_button)
            time.sleep(0.2)

    def check_closed_left_menu_history_button(self):
        with allure.step("Проверка наличия кнопки История при закрытом меню"):
            self.click_element(main_page_locators.closed_history_button)
            time.sleep(0.2)

#проверка наличия категорий

    def check_categories(self):
        with allure.step("Проверка наличия категорий"):
            categories = self.driver.find_elements(By.CSS_SELECTOR, main_page_locators.categories)
            for category in categories:
                category.click()
                time.sleep(0.5)

#проверка видео

    def check_videos(self):
        with allure.step("Проверка наличия видео"):
            videos = self.driver.find_elements(By.XPATH, main_page_locators.videos)

            for video in videos[0:5]:
                video.click()
                self.wait_for_page_to_load(self.driver)
                self.driver.back()
                time.sleep(0.2)

    def check_videos_img(self):
        with allure.step("Проверка наличия превью у видео"):
            videos_img = self.driver.find_elements(By.XPATH, main_page_locators.videos_img)

            for video_img in videos_img[0:5]:
                video_img.is_displayed()
                time.sleep(0.2)

#проверка авторизации

    def check_login(self):
        with allure.step("Проверка авторизации"):
            login = 'testingseleneum@gmail.com'
            password = 'superslozniyparolniktonehaknet123'

            self.click_element(main_page_locators.header_login_button)
            self.wait_for_page_to_load(self.driver)
            self.driver.find_element(By.CSS_SELECTOR, main_page_locators.email_field).send_keys(login)
            self.driver.find_element(By.CSS_SELECTOR, main_page_locators.next_button).click()
            self.wait_for_page_to_load(self.driver)
            time.sleep(5)
            self.driver.find_element(By.CSS_SELECTOR, main_page_locators.password_field).send_keys(password)
            self.driver.find_element(By.CSS_SELECTOR, main_page_locators.next_button).click()
            self.wait_for_page_to_load(self.driver)

#проверка хэдэра (пользователь вошел в акк)

    def check_user_old_header_buttons(self):
        with allure.step("Проверка наличия старых кнопок хэдэра"):

            self.check_header_burger_button()
            self.check_header_logo_button()
            self.check_header_search_field()
            self.check_header_keyboard_button()
            self.check_header_search_button()
            self.check_header_voice_search_button()

    def check_user_create_button(self):
        with allure.step("Проверка наличия кнопки Создать"):
            self.click_element(main_page_locators.create_button)

    def check_user_notifications_button(self):
        with allure.step("Проверка наличия кнопки Уведомления"):
            self.click_element(main_page_locators.notifications_button)

    def check_user_avatar_button(self):
        with allure.step("Проверка наличия кнопки аватара"):
            self.click_element(main_page_locators.avatar_button)

