from selenium.webdriver.common.by import By
import sys
from time import sleep
from page.videopage import VideoPage
from os.path import dirname
BASE_PATH = dirname(dirname(__file__))
sys.path.append(BASE_PATH)


class MusicPage(VideoPage):
    music_23 = (By.XPATH, "//android.widget.TextView[contains(@text,'23_MP3_44.1KHz_128Kbps_2ch.mp3')]\
        /../android.widget.ImageView[1]")
    music_23_name = (By.XPATH, "//android.widget.TextView[contains(@text,'23_MP3_44.1KHz_128Kbps_2ch.mp3')]")
    music_24 = (By.XPATH, "//android.widget.TextView[contains(@text,'24_WMA_Pro9.1_44.1KHz_24bits_200Kbps_2ch_VBR.wma')]\
            /../android.widget.ImageView[1]")
    music_24_name = (
    By.XPATH, "//android.widget.TextView[contains(@text,'24_WMA_Pro9.1_44.1KHz_24bits_200Kbps_2ch_VBR.wma')]")
    music_25 = (By.XPATH, "//android.widget.TextView[contains(@text,'25_PCM_44.1KHz_705Kbps_16bit_1ch.wav')]\
        /../android.widget.ImageView[1]")
    music_25_name = (By.XPATH, "//android.widget.TextView[contains(@text,'25_PCM_44.1KHz_705Kbps_16bit_1ch.wav')]")
    music_26 = (By.XPATH, "//android.widget.TextView[contains(@text,'26_DTS_44.1KHz_1411.2Kbps_24Bit_2ch.wav')]\
        /../android.widget.ImageView[1]")
    music_26_name = (By.XPATH, "//android.widget.TextView[contains(@text,'26_DTS_44.1KHz_1411.2Kbps_24Bit_2ch.wav')]")
    music_27 = (By.XPATH, "//android.widget.TextView[contains(@text,'27_AAC-v4_LC_44.1KHz_43FPS_2ch.aac')]\
        /../android.widget.ImageView[1]")
    music_27_name = (By.XPATH, "//android.widget.TextView[contains(@text,'27_AAC-v4_LC_44.1KHz_43FPS_2ch.aac')]")
    music_28 = (By.XPATH, "//android.widget.TextView[contains(@text,'28_Vorbis_16.0KHz_600Kbps_6ch.ogg')]\
        /../android.widget.ImageView[1]")
    music_28_name = (By.XPATH, "//android.widget.TextView[contains(@text,'28_Vorbis_16.0KHz_600Kbps_6ch.ogg')]")
    music_page = (By.XPATH, "//android.widget.TextView[contain(@text,'Music')]")
    music_previous = (By.ID, "com.eswin.tv.filebrowser:id/btnToPrevious")
    music_next = (By.ID, "com.eswin.tv.filebrowser:id/btnToNext")
    music_pause = (By.ID, "com.eswin.tv.filebrowser:id/btnPause")
    audio_tv_time = (By.ID, "com.eswin.tv.filebrowser:id/audio_tv_time")
    audio_end_time = (By.ID, "com.eswin.tv.filebrowser:id/audio_end_time")
    music_page_number = 6

    def music_page_switch(self):
        for i in range(3):
            self.driver.keyevent(22)

    def click_music_previous(self):
        self.find_element(*self.music_previous).click()
        self.driver.keyevent(23)

    def click_music_next(self):
        self.find_element(*self.music_next).click()
        self.driver.keyevent(23)

    def click_music_23(self):
        self.video_find(*self.music_23, n=self.music_page_number)

    def click_music_24(self):
        self.video_find(*self.music_24, n=self.music_page_number)

    def click_music_25(self):
        self.video_find(*self.music_25, n=self.music_page_number)

    def click_music_26(self):
        self.video_find(*self.music_26, n=self.music_page_number)

    def click_music_27(self):
        self.video_find(*self.music_27, n=self.music_page_number)

    def click_music_28(self):
        self.video_find(*self.music_28, n=self.music_page_number)

    def playback_music(self, *name):
        result, result2 = False, False
        for i in range(1):
            self.driver.keyevent(23)
            sleep(2)
            self.driver.keyevent(23)
            self.driver.keyevent(23)
            sleep(2)
            self.click_music_previous()
            sleep(1)
            self.driver.keyevent(22)
            self.driver.keyevent(23)
            self.click_music_next()
            sleep(5)
            self.driver.keyevent(21)
            self.driver.keyevent(23)
            if i == 0:
                result = self.time_judge(*self.audio_tv_time)
                result2 = self.name_judge(*name)
            sleep(1)
            self.driver.keyevent(4)
            self.driver.keyevent(4)
        return result & result2
