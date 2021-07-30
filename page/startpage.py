#!usr/bin/python3
# -*- coding: utf-8 -*-
# @time      : 2021/4/13 9:07
# @author    : zhuziqing
# @File      : startpage.py
from selenium.webdriver.common.by import By
import sys
from app_config import CAPS1, CAPS
from appium import webdriver
from time import sleep
from retry import retry
from page.basepage import BasePage
from os.path import dirname
BASE_PATH = dirname(dirname(__file__))
sys.path.append(BASE_PATH)

class StartPage(BasePage):
    power_off_button = (By.XPATH, "//android.widget.ListView/android.widget.LinearLayout[2]")
    restart_button = (By.XPATH, "//android.widget.ListView/android.widget.LinearLayout[3]")
    HDMI_1 = (By.XPATH, "//android.widget.TextView[contains(@text,'HDMI-1')]")
    setting_About = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[8]")
    setting_System_Info = (By.ID, "com.eswin.tv.settings:id/layout_system_info")
    setting_System_Version = (By.ID, "com.eswin.tv.settings:id/tv_system_version")
    count = 0

    def setting_About_click(self):
        self.driver.find_element(*self.setting_About).click()
        self.driver.keyevent(23)

    def setting_System_Info_click(self):
        self.driver.find_element(*self.setting_System_Info).click()
        self.driver.keyevent(23)

    def setting_System_Version_judge(self):
        el = self.driver.find_element(*self.setting_System_Version)
        print(el.text)
        if el.text == 'Android 11':
            return True
        else:
            return False

    def power_off(self):
        self.driver.long_press_keycode(26)
        self.driver.find_element(*self.power_off_button).click()
        sleep(10)
        self.driver.keyevent(26)

    def restart(self):
        #self.check_port('127.0.0.1', 4723)
        self.driver.long_press_keycode(26)
        self.driver.find_element(*self.restart_button).click()

    @retry(tries=2, delay=75)
    def restart_judge(self):
        if self.count == 0:
            self.count += 1
            self.restart()
        if self.count == 1:
            # os.system("adb uninstall io.appium.uiautomator2.server")
            # sleep(2)
            # os.system("adb uninstall io.appium.uiautomator2.server.test")
            # sleep(2)
            # os.system('start docker exec -it appium1 adb connect 10.11.0.86:5555')
            # sleep(3)
            driver = webdriver.Remote("http://localhost:4723/wd/hub", CAPS1)
            driver.implicitly_wait(10)
            self.count = 0
            self.driver = driver
            driver.keyevent(3)
            driver.keyevent(20)
            driver.keyevent(19)
            try:
                driver.find_element(*self.HDMI_1)
            except Exception as e:
                # driver.quit()
                return False
            else:
                print("yessssss")
                # driver1.quit()
                # driver.quit()
                return True


    def app_start(self, driver):
        result = False
        driver2 = webdriver.Remote("http://localhost:4723/wd/hub", CAPS1)
        self.driver = driver2
        for i in range(3):
            driver2.start_activity("com.eswin.tv.filebrowser", ".home.HomePageActivity")
            try:
                self.find_element(*self.video_page)
                print("ok")
            except Exception as e:
                print("app未正常打开")

            else:
                driver.keyevent(4)
                try:
                    self.find_element(*self.HDMI_1)
                except Exception as e:
                    print("app未正常退出")

                else:
                    result = True
        driver2.quit()
        return result

