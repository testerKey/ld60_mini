#!usr/bin/python3
# -*- coding: utf-8 -*-
# @time      : 2021/4/8 11:05
# @author    : zhuziqing
# @File      : videopage.py
from selenium.webdriver.common.by import By
from time import sleep
from page.basepage import BasePage
from time import perf_counter
import sys
from os.path import dirname
BASE_PATH = dirname(dirname(__file__))
sys.path.append(BASE_PATH)

class VideoPage(BasePage):

    video_19 = (By.XPATH, "//android.widget.TextView[contains(@text,'19_H264_High@L4_1920x1056@23.976fps_4890Kbps_PCM_44.1KHz_16Bit_2ch.mkv')]\
    /../android.widget.ImageView[1]")
    video_19_name = (By.XPATH, "//android.widget.TextView[contains(@text,'19_H264_High@L4_1920x1056@23.976fps_4890Kbps_PCM_44.1KHz_16Bit_2ch.mkv')]")
    video_15 = (By.XPATH, "//android.widget.TextView[contains(@text,'15_H264_Baseline@L4_1920x1080@29.97fps_8002Kbps_MP3_44.1KHz_128Kbps_2ch.mp4')]\
    /../android.widget.ImageView[1]")
    video_15_name = (By.XPATH, "//android.widget.TextView[contains(@text,'15_H264_Baseline@L4_1920x1080@29.97fps_8002Kbps_MP3_44.1KHz_128Kbps_2ch.mp4')]")
    video_16 = (By.XPATH, "//android.widget.TextView[contains(@text,'16_H265_Main@L4.1_1920x1080@19.98fps_800Kbps_ADPCM_ALAW_8KHz_64Kbps_1ch.mp4')]\
    /../android.widget.ImageView[1]")
    video_16_name = (By.XPATH, "//android.widget.TextView[contains(@text,'16_H265_Main@L4.1_1920x1080@19.98fps_800Kbps_ADPCM_ALAW_8KHz_64Kbps_1ch.mp4')]")
    video_17 = (By.XPATH, "//android.widget.TextView[contains(@text,'17_MPEG2_Simple@Main_480x360@30fps_1543Kbps_8bit_AAC-LC_48.0KHz_128Kbps_2ch.mp4')]\
    /../android.widget.ImageView[1]")
    video_17_name = (By.XPATH, "//android.widget.TextView[contains(@text,'17_MPEG2_Simple@Main_480x360@30fps_1543Kbps_8bit_AAC-LC_48.0KHz_128Kbps_2ch.mp4')]")
    video_18 = (By.XPATH, "//android.widget.TextView[contains(@text,'18_MPEG4_Simple@L1_1280x720_3624kbps_30p_MP3.mp4')]\
    /../android.widget.ImageView[1]")
    video_18_name = (By.XPATH, "//android.widget.TextView[contains(@text,'18_MPEG4_Simple@L1_1280x720_3624kbps_30p_MP3.mp4')]")
    video_20 = (By.XPATH, "//android.widget.TextView[contains(@text,'20_VP9_1920x1080@nofps_1687kbps_Vobis_44.1KHz_128Kbps_VBR_2ch.mkv')]\
    /../android.widget.ImageView[1]")
    video_20_name = (By.XPATH, "//android.widget.TextView[contains(@text,'20_VP9_1920x1080@nofps_1687kbps_Vobis_44.1KHz_128Kbps_VBR_2ch.mkv')]")
    video_21 = (By.XPATH, "//android.widget.TextView[contains(@text,'21_mpeg-ts_Sisvel3DTile.ts')]/../android.widget.ImageView[1]")
    video_21_name = (By.XPATH, "//android.widget.TextView[contains(@text,'21_mpeg-ts_Sisvel3DTile.ts')]")
    video_22 = (By.XPATH, "//android.widget.TextView[contains(@text,'22_MPEG-PS_XinBaiNiangZiChuanQi.mpg')]/../android.widget.ImageView[1]")
    video_22_name = (By.XPATH, "//android.widget.TextView[contains(@text,'22_MPEG-PS_XinBaiNiangZiChuanQi.mpg')]")
    video_29 = (By.XPATH, "//android.widget.TextView[contains(@text,'MPEG-4(DivX 5)_SP@L3_720x400@25fps_82.3Kbps_MP3_48.0KHz_96.0Kbps_1ch.avi')]\
    /../android.widget.ImageView[1]")
    video_29_name = (By.XPATH, "//android.widget.TextView[contains(@text,'MPEG-4(DivX 5)_SP@L3_720x400@25fps_82.3Kbps_MP3_48.0KHz_96.0Kbps_1ch.avi')]")
    video_54 = (By.XPATH, "//android.widget.TextView[contains(@text,'B1_MPEG-4(DivX 5)_SP@L3_720x400@25.000fps_621Kbps_MP3_48.0KHz_96.0Kbps_2ch.avi')]\
    /../android.widget.ImageView[1]")
    video_54_name = (By.XPATH, "//android.widget.TextView[contains(@text,'B1_MPEG-4(DivX 5)_SP@L3_720x400@25.000fps_621Kbps_MP3_48.0KHz_96.0Kbps_2ch.avi')]")
    video_55 = (By.XPATH, "//android.widget.TextView[contains(@text,'AVC_High@L4_1920x1080@25fps_14.3Mbps_2Audio_AC-3_48KHz_苏慧伦 - 旋转门.mpg')]\
    /../android.widget.ImageView[1]")
    # video播放暂停
    puase_user = (By.ID, "com.eswin.tv.filebrowser:id/pause_user")
    # 进入video页面
    video_page = (By.XPATH, "//android.widget.TextView[contains(@text,'Video')]/../android.widget.TextView[2]")
    # 菜单键进入
    audio_track = (By.XPATH, "//android.widget.TextView[contains(@text,'audio_track')]")
    # 菜单键进入
    subtitle_sel = (By.XPATH, "//android.widget.TextView[contains(@text,'subtitle_selection')]")
    # Video当前播放进度
    time_current = (By.ID, "com.eswin.tv.filebrowser:id/time_current")
    # Video文件列表resource-id
    video_elements = (By.ID, "com.eswin.tv.filebrowser:id/videoitem_name")
    # 定义Video文件个数
    video_page_number = 10
    #进入filebrowser后右键进入Video
    def video_page_switch(self):
        self.driver.keyevent(22)

    def video_find(self, *video_name, n):  # 顺序查找
        time = perf_counter()
       # i = j = 0
       #  while 1:
       #      try:  # 判定播放正常退出
       #          self.find_elements(*self.video_elements)
       #      except Exception as e:
       #          # 返回
       #          self.driver.keyevent(4)
       #          self.driver.keyevent(4)
       #      else:
       #          break
        for j in range(n):  # 初始化索引位置
            self.driver.keyevent(19)
        for i in range(n//2):
            try:
                self.driver.find_element(*video_name).click()
            except Exception as e:
                for k in range(2):
                    self.driver.keyevent(20)
            else:
                break
        time1 = perf_counter()
        print(time1-time)
        time1 = perf_counter()
        print(time1-time)

    def click_video_19(self):
        self.video_find(*self.video_19, n=self.video_page_number)

    def click_video_15(self):
        self.video_find(*self.video_15, n=self.video_page_number)

    def click_video_16(self):
        self.video_find(*self.video_16, n=self.video_page_number)

    def click_video_17(self):
        self.video_find(*self.video_17, n=self.video_page_number)

    def click_video_18(self):
        self.video_find(*self.video_18, n=self.video_page_number)

    def click_video_20(self):
        self.video_find(*self.video_20, n=self.video_page_number)

    def click_video_21(self):
        self.video_find(*self.video_21, n=self.video_page_number)

    def click_video_22(self):
        self.video_find(*self.video_22, n=self.video_page_number)

    def click_video_29(self):
        self.video_find(*self.video_29, n=self.video_page_number)

    def click_video_54(self):
        self.video_find(*self.video_54, n=self.video_page_number)

    # def click_video_55(self):
    #     self.video_find(*self.video_55, n=self.video_page_number)

    def time_judge(self, *name):
        time = perf_counter()
        try:
            el = self.driver.find_element(*name)
        except Exception as e:
            print("没找到")
            return False
        else:
            time1 = (el.text.split(':'))[-1]
            if time1[0] == '0':
                time1 = time1[1]
            if eval(time1) > 0:
                time1 = perf_counter()
                print(time1 - time)
                return True

    def name_judge(self, *name):
        try:
            self.driver.find_element(*name)
        except Exception as e:
            print("播放的不是对应文件")
            return False
        else:
            return True

    def playback_video(self, *name):
        self.driver.keyevent(23)  # 播放
        self.driver.long_press_keycode(22)  # seek
        self.driver.keyevent(23)
        self.driver.long_press_keycode(22)
        sleep(5)
        self.driver.keyevent(23)
        print('playback_after_sleep')
        result1 = self.time_judge(*self.time_current)
        result2 = self.name_judge(*name)
        sleep(5)
        self.driver.keyevent(4)
        self.driver.keyevent(4)
        return result1 & result2

    def switch_audio_track(self, audiotrack_number):
        audiotrack_box = (By.XPATH, "//android.widget.RadioButton[contains(@text,'Audio track%d(und)')]" % audiotrack_number)
        for i in range(2):
            self.driver.keyevent(23)
            sleep(8)

            self.driver.keyevent(82)  # 菜单键
            try:
                self.find_element(*self.audio_track)
            except Exception as e:
                print("未找到audio track")
            else:
                self.driver.keyevent(20)
                self.driver.keyevent(23)
                try:
                    el = self.find_element(*audiotrack_box)
                except Exception as e:
                    print("未见第{}路音轨".format(audiotrack_number))
                    return False
                else:
                    print("找到元素")
                    if i == 0:
                        self.driver.keyevent(20)
                        self.driver.keyevent(23)
                    else:
                        if el.get_attribute("checked") == 'true':
                            return True
