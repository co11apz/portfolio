import time

import allure
from selenium.common import NoSuchElementException

from Roman_Malajev.diplom.pages.base_page import BasePage

from Roman_Malajev.diplom.pages.locators import video_page_locators


class Header(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_page(self):
        with allure.step("Проверка перехода на главную страницу"):
            self.driver.get('https://www.youtube.com/')

    def check_videoplayer_items(self):
        with allure.step("Проверка кнопок видеоплеера"):
            videoplayer_elements = [
                video_page_locators.play_button,
                video_page_locators.next_video_button,
                video_page_locators.mute_volume_button,
                video_page_locators.autoplay_button,
                video_page_locators.subtitles_button,
                video_page_locators.settings_button,
                video_page_locators.mini_player_button,
                video_page_locators.wide_screen_button,
                video_page_locators.full_screen_button
            ]

            BasePage.check_elements_click(videoplayer_elements)