from selenium.webdriver.common.by import By

#video_section
play_button = (By.XPATH, '(//button[@class="ytp-play-button ytp-button"])[1]')
next_video_button = (By.XPATH, '(//a[@class="ytp-next-button ytp-button"])[1]')
mute_volume_button = (By.XPATH, '(//button[@class="ytp-mute-button ytp-button"])[1]')
autoplay_button = (By.XPATH, '(//button[@class="ytp-button"])[1]')
subtitles_button = (By.XPATH, '(//button[@class="ytp-subtitles-button ytp-button"])[1]')
settings_button = (By.XPATH, '(//button[@class="ytp-button ytp-settings-button"])[1]')
mini_player_button = (By.XPATH, '(//button[@class="ytp-miniplayer-button ytp-button"])[1]')
wide_screen_button = (By.XPATH, '(//button[@class="ytp-size-button ytp-button"])[1]')
full_screen_button = (By.XPATH, '(//button[@class="ytp-fullscreen-button ytp-button"])[1]')

#under_video_section
subscribe_button = (By.CSS_SELECTOR, '[class="yt-spec-button-shape-next yt-spec-button-shape-next--filled yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m"]')
like_button = (By.XPATH, '(//button[@class="yt-spec-button-shape-next yt-spec-button-shape-next--tonal yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-leading yt-spec-button-shape-next--segmented-start"])[1]')
dislike_button = (By.XPATH, '(//button[@class="yt-spec-button-shape-next yt-spec-button-shape-next--tonal yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m yt-spec-button-shape-next--icon-button yt-spec-button-shape-next--segmented-end"])[1]')