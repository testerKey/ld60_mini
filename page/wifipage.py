import sys
import os
import socket
from retry import retry
from appium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from page.videopage import VideoPage
from app_config import CAPS1, CAPS
from os.path import dirname
BASE_PATH = dirname(dirname(__file__))
sys.path.append(BASE_PATH)


class WifiPage(VideoPage):
    wifi_path = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]")
    network_path = (By.XPATH, "//android.view.ViewGroup/android.view.ViewGroup[1]")
    detection_path = (By.XPATH, "//android.view.ViewGroup/android.view.ViewGroup[3]")
    detection_result_path = (By.XPATH,
                             "//android.widget.TextView[contains(@text,'Everything is normal on the network')]")
    targetwifi_path = (By.XPATH, "//android.widget.TextView[contains(@text,'ESWIN-HF02')]")
    targetwifi_key = 'Eswin888888'
    connect_path = (By.XPATH, "//android.widget.TextView[contains(@text,'Connected')]")
    ip_path = (By.XPATH, "//android.widget.TextView[contains(@text,'Network Ip')]")
    ignore_path = (By.XPATH, "//android.widget.TextView[contains(@text,'Ignore This Network')]")
    password_id = (By.ID, "com.eswin.tv.settings:id/et_info")
    open_id = (By.XPATH, "//android.widget.TextView[contains(@text,'Open')]")
    off_id = (By.XPATH, "//android.widget.TextView[contains(@text,'Off')]")
    restart_button = (By.XPATH, "//android.widget.ListView/android.widget.LinearLayout[3]")
    shortvideo = (By.XPATH, "//android.widget.TextView[contains(@text,'随刻热点')]")
    yh_play_time = (By.ID, "com.gitvdemo.video:id/play_text_video_time")
    yh_app_manager = (By.XPATH, "//android.widget.TextView[contains(@text,'银河奇异果')]/..")
    yhTV = (By.XPATH, "//android.widget.TextView[contains(@text,'银河奇异果')]/../android.widget.ImageView[1]")
    jg_continue_button = (By.ID, "com.android.permissioncontroller:id/continue_button")
    apk_exit_button = (By.XPATH, "//android.widget.TextView[contains(@text,'退出不看了')]")
    apk_open_button = (By.ID, "android:id/button1")
    app_uninstall_button = (By.ID, "com.eswin.tv.appmanager:id/iv_uninstall")
    wifi_enable = (By.ID, "com.eswin.tv.settings:id/iv_right_enable_wifi")
    iqiyi_path = "C:\\apk\\qiyiguo_official11.6.3.apk"
    # test_server = ('www.baidu.com', 443)
    count = 0

    def open_wifi(self):
        self.driver.start_activity("com.eswin.tv.settings", ".home.HomeActivity")
        self.wireless_click()
        try:
            self.find_element(*self.open_id).click()
        except:
            self.find_element(*self.wifi_enable).click()
            self.driver.keyevent(21)
            sleep(5)

    def close_wifi(self):
        self.driver.start_activity("com.eswin.tv.settings", ".home.HomeActivity")
        self.wireless_click()
        sleep(5)
        try:
            self.find_element(*self.off_id)
        except:
            self.find_element(*self.wifi_enable).click()
            self.driver.keyevent(21)

    def connect_wifi(self):
        self.open_wifi()
        self.find_element(*self.targetwifi_path).click()
        self.driver.keyevent(23)
        try:
            self.driver.find_element(*self.password_id).send_keys(*self.targetwifi_key)
        except:
            for i in range(5):
                self.driver.keyevent(20)
            self.driver.find_element(*self.password_id).send_keys(*self.targetwifi_key)
        sleep(1)
        self.driver.keyevent(66)

    def network_check_all(self):
        result = []
        self.driver.start_activity("com.eswin.tv.settings", ".home.HomeActivity")
        self.wireless_click()
        result.append(self.keyword_check())  # 关键字connect检查网络
        self.driver.keyevent(4)
        self.detection_click()
        result.append(self.detection_result_check())  # detection检查网络
        return result

    def install_apk(self, path):
        os.system('adb install %s' % path)
        sleep(10)

    def uinstall_yh(self):
        self.uninstall_apk(*self.yh_app_manager)
        try:
            self.driver.keyevent(3)
            self.driver.keyevent(20)
            self.driver.keyevent(20)
            self.find_element(*self.yhTV).click()
        except Exception as e:
            print("银河奇异果已成功卸载")
            return True
        else:
            print("卸载失败")
            return False

    def uninstall_apk(self, *package_name):
        self.driver.start_activity(" com.eswin.tv.appmanager", ".ui.activity.AppActivity")
        for i in range(3):  # 卸载app
            try:
                self.find_element(*package_name).click()
            except Exception as e:
                self.driver.keyevent(20)
            else:
                self.driver.keyevent(23)
                try:
                    self.find_element(*self.app_uninstall_button).click()
                except Exception as e:
                    print("此app不能卸载，请选择其他app")
                    self.driver.keyevent(20)
                else:
                    self.driver.keyevent(23)
                    self.driver.keyevent(21)
                    self.driver.keyevent(23)
                    break
        # 等待卸载
        sleep(10)
        self.driver.keyevent(4)  # 退出appmanager

    def switch_iqiyi(self):
        self.switch_iqiyi_sec()
        self.find_element(*self.jg_continue_button).click()
        self.driver.keyevent(23)

    def switch_iqiyi_sec(self):
        self.driver.keyevent(3)
        self.driver.keyevent(20)
        self.driver.keyevent(20)
        self.driver.keyevent(20)
        self.find_element(*self.yh_app_manager).click()
        self.driver.keyevent(23)

    def playback_yh(self):
        self.driver.keyevent(4)
        self.playback_yh_sec()

    def playback_yh_sec(self):
        result = False
        try:  # 进入app后进入短视频页
            self.find_element(*self.shortvideo).click()
        except Exception as e:
            print("app启动失败")
        else:  # 播放短视频并抓取时间戳
            self.driver.keyevent(23)
            self.driver.keyevent(23)
            sleep(10)
            self.driver.keyevent(23)
            result = self.time_judge(*self.yh_play_time)
            print("app运行正常")
        # 退出apk
        for i in range(4):
            try:
                self.find_element(*self.apk_exit_button).click()
            except Exception as e:
                if i == 2:
                    self.driver.keyevent(4)
                else:
                    self.driver.keyevent(4)
                    self.driver.keyevent(4)
            else:
                sleep(3)
                self.driver.keyevent(23)
                break
        return result

    def wireless_click(self):
        self.find_element(*self.wifi_path).click()
        self.driver.keyevent(23)
        self.find_element(*self.network_path).click()  # 此处已点击,不需要keyevent(23)
        sleep(5)

    def disconnect_wifi(self):
        self.open_wifi()
        self.wireless_click()
        self.find_element(*self.targetwifi_path).click()
        self.driver.keyevent(23)
        self.find_element(*self.ip_path).click()
        self.driver.keyevent(23)
        self.find_element(*self.ignore_path).click()
        self.driver.keyevent(23)

    def detection_click(self):
        # self.find_element(*self.wifi_path).click()
        self.find_element(*self.detection_path).click()
        self.driver.keyevent(23)
        sleep(10)

    def keyword_check(self):
        try:
            self.find_element(*self.connect_path)
            print('hf02 is connected')
            return True
        except:
            return False

    def detection_result_check(self):
        try:
            self.find_element(*self.detection_result_path)
            print('Everything is normal on the network')
            return True
        except:
            self.driver.keyevent(4)
            return False

    def restart(self):
        self.driver.long_press_keycode(26)
        self.find_element(*self.restart_button).click()

    @retry(tries=2, delay=75)
    def restart_judge(self):
        self.driver.keyevent(3)
        if self.count == 0:
            self.count += 1
            self.restart()
        if self.count == 1:
            driver = webdriver.Remote("http://localhost:4723/wd/hub", CAPS1)
            driver.implicitly_wait(10)
            self.count = 0
            self.driver = driver
            driver.start_activity('com.eswin.tv.settings', '.home.HomeActivity')
            self.wireless_click()
            result = self.keyword_check()
            return result

    # def baidu_check(self):
    #     s = socket.socket()
    #     s.settimeout(3)
    #
    #     try:
    #         status = s.connect_ex(self.test_server)
    #         if status == 0:
    #             s.close()
    #             print('baidu is connected')
    #             return True
    #         else:
    #             return False
    #     except Exception as e:
    #         return False

