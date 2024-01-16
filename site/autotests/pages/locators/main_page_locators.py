from selenium.webdriver.common.by import By

#header
search_field = (By.CSS_SELECTOR, '[placeholder="Введите запрос"]')
search_button = (By.CSS_SELECTOR, '[id="search-icon-legacy"]')
burger_button = (By.XPATH, '//div[@id="start"]//yt-icon-button[@id="guide-button"]')
keyboard_button = (By.CSS_SELECTOR, '[id="gs_st50"]')
options_button = (By.XPATH, '(//button[@aria-label="Настройки"])[1]')
header_login_button = (By.XPATH, '(//ytd-button-renderer[@class="style-scope ytd-masthead"])[3]')
voice_search_button = (By.CSS_SELECTOR, '[class="yt-spec-touch-feedback-shape yt-spec-touch-feedback-shape--overlay-touch-response"]')
logo_button = (By.XPATH, '(//a[@class="yt-simple-endpoint style-scope ytd-topbar-logo-renderer"])[1]')
dop_cancel_button = (By.XPATH, '(//button[@class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-only-default"])[4]')

#header_settings
your_data_button = (By.CSS_SELECTOR, '[href="https://myaccount.google.com/u/0/yourdata/youtube?hl=ru"]')
theme_button = (By.CSS_SELECTOR, '[role="option"]')
language_button = (By.XPATH, '(//a[@class="yt-simple-endpoint style-scope ytd-compact-link-renderer"])[2]')
safemode_button = (By.XPATH, '(//div[@id="items"]//ytd-compact-link-renderer[@class="style-scope yt-multi-page-menu-section-renderer"])[3]')
country_button = (By.XPATH, '(//div[@id="items"]//ytd-compact-link-renderer[@class="style-scope yt-multi-page-menu-section-renderer"])[4]')
hotkeys_button = (By.XPATH, '(//div[@id="items"]//ytd-compact-link-renderer[@class="style-scope yt-multi-page-menu-section-renderer"])[5]')
inoptions_button = (By.XPATH, '(//div[@id="items"]//ytd-compact-link-renderer[@class="style-scope yt-multi-page-menu-section-renderer"])[6]')
inabout_button = (By.XPATH, '(//div[@id="items"]//ytd-compact-link-renderer[@class="style-scope yt-multi-page-menu-section-renderer"])[7]')
insend_report_button = (By.XPATH, '(//div[@id="items"]//ytd-compact-link-renderer[@class="style-scope yt-multi-page-menu-section-renderer"])[8]')
back_button = (By.XPATH, '(//button[@class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-only-default"])[4]')
close_button = (By.CSS_SELECTOR, '[class="yt-spec-button-shape-next yt-spec-button-shape-next--text yt-spec-button-shape-next--call-to-action yt-spec-button-shape-next--size-m"]')
help_close_button = (By.XPATH, '//button[@class="help-panel-header__close-button"]')
report_close_button = (By.XPATH, '(//button[@class="scSharedMaterialbuttonroot scSharedMaterialbuttontext scSharedMaterialbuttoncolor-label scSharedMaterialbuttonicon-only"])[2]')
menu_container = (By.XPATH, '(//div[@class="menu-container style-scope ytd-multi-page-menu-renderer"])[1]')
iframe_help = (By.CSS_SELECTOR, '[id="help_panel_main_frame"]')
iframe_feedback = (By.CSS_SELECTOR, '[id="google-feedback-iframe"]')

#left menu
history_button = (By.XPATH, '(//a[@href="/feed/history"])[1]')
subscriptions_button = (By.XPATH, '(//a[@href="/feed/subscriptions"])[1]')
shorts_button = (By.XPATH, '(//a[@id="endpoint" and @title="Shorts"])[1]')
left_login_button = (By.XPATH, '//ytd-button-renderer[@class="style-scope ytd-guide-signin-promo-renderer"]')
main_button = (By.XPATH, '(//a[@href="/" and @title="Главная"])[1]')
you_button = (By.XPATH, '(//a[@href="/feed/you" and @title="Вы"])[1]')
trend_button = (By.XPATH, '(//a[@title="В тренде"])[1]')
music_button = (By.XPATH, '(//a[@title="Музыка"])[1]')
translations_button = (By.XPATH, '(//a[@title="Трансляции"])[1]')
videogames_button = (By.XPATH, '(//a[@title="Видеоигры"])[1]')
sport_button = (By.XPATH, '(//a[@title="Спорт"])[1]')
catalogue_button = (By.CSS_SELECTOR, '[href="/feed/guide_builder"]')
premium_button = (By.CSS_SELECTOR, '[href="/premium"]')
yt_music_button = (By.CSS_SELECTOR, '[href="https://music.youtube.com/"]')
yt_kids_button = (By.CSS_SELECTOR, '[href="https://www.youtubekids.com/?source=youtube_web"]')
settings_button = (By.XPATH, '//a[@href="/account" and @title="Настройки"]')
reports_button = (By.XPATH, '//a[@href="/reporthistory"]')
about_button = (By.XPATH, '//a[@title="Справка"]')
send_report_button = (By.XPATH, '//a[@title="Отправить отзыв"]')

#left menu close buttons
closed_main_button = (By.CSS_SELECTOR, 'ytd-mini-guide-entry-renderer[aria-label="Главная"]')
closed_shorts_button = (By.CSS_SELECTOR, 'ytd-mini-guide-entry-renderer[aria-label="Shorts"]')
closed_subscriptions_button = (By.CSS_SELECTOR, 'ytd-mini-guide-entry-renderer[aria-label="Подписки"]')
closed_you_button = (By.CSS_SELECTOR, 'ytd-mini-guide-entry-renderer[aria-label="Вы"]')
closed_history_button = (By.CSS_SELECTOR, 'ytd-mini-guide-entry-renderer[aria-label="История"]')

#categories
categoria_music_button = (By.XPATH, '//yt-formatted-string[@id="text" and @title="Музыка"]')
categoria_videogames_button = (By.XPATH, '//yt-formatted-string[@id="text" and @title="Видеоигры"]')
categoria_streams_button = (By.XPATH, '//yt-formatted-string[@id="text" and @title="Сейчас в эфире"]')
categoria_sitcoms_button = (By.XPATH, '//yt-formatted-string[@id="text" and @title="Ситкомы"]')
categoria_sketch_button = (By.XPATH, '//yt-formatted-string[@id="text" and @title="Скетч-шоу"]')
categoria_animation_button = (By.XPATH, '//yt-formatted-string[@id="text" and @title="Анимация"]')
categoria_rap_button = (By.XPATH, '//yt-formatted-string[@id="text" and @title="Рэп"]')
categoria_action_and_adventures_button = (By.XPATH, '//yt-formatted-string[@id="text" and @title="Экшен и приключения"]')
categoria_nature_button = (By.XPATH, '//yt-formatted-string[@id="text" and @title="Природа"]')
categoria_recently_published_button = (By.XPATH, '//yt-formatted-string[@id="text" and @title="Недавно опубликованные"]')
categories = 'yt-chip-cloud-chip-renderer[class="style-scope ytd-feed-filter-chip-bar-renderer"]'

#videos
videos = '//div[@class="style-scope ytd-rich-item-renderer"]'
videos_img = '//div[@id="content"]//img[@style="background-color: transparent;"]'

#login
email_field = '[type="email"]'
password_field = '[type="password"]'
next_button = '[class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b"]'
not_now_button = '[class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-dgl2Hf ksBjEc lKxP2d LQeN7 k97fxb yu6jOd"]'

#header user
create_button = (By.CSS_SELECTOR, '[class="style-scope ytd-topbar-menu-button-renderer style-default"]')
notifications_button = (By.CSS_SELECTOR, '[aria-label="Уведомления"]')
avatar_button = (By.CSS_SELECTOR, '[id="avatar-btn"]')