from selenium.webdriver.common.by import By
import sys
from random import randint, choice
from time import sleep
from appium import webdriver
from page.basepage import BasePage
from os.path import dirname
from retry import retry
from app_config import CAPS1
BASE_PATH = dirname(dirname(__file__))
sys.path.append(BASE_PATH)


class AudioPage(BasePage):

    balance_layout = (By.ID, 'com.eswin.tv.settings:id/layout_balance')  # audio界面BalanceID
    balance_switch = (By.ID, 'com.eswin.tv.settings:id/tv_switch_balance')  # audio界面Balance值ID
    setting_Audio = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[6]")  # setting->audi
    audio_mode_layout = (By.ID, "com.eswin.tv.settings:id/layout_audio_mode")  # audio界面AudioModeID
    audio_mode_name = (By.ID, "com.eswin.tv.settings:id/tv_name_type")  # AudioMode界面Customize
    eq0_value = (By.ID, "com.eswin.tv.settings:id/tv_value_eq0")
    eq2_value = (By.ID, "com.eswin.tv.settings:id/tv_value_eq2")
    eq4_value = (By.ID, "com.eswin.tv.settings:id/tv_value_eq4")
    restart_button = (By.XPATH, "//android.widget.ListView/android.widget.LinearLayout[3]")
    count = 0

    # setting界面->audio界面->选中balance焦点
    def balance_layout_click(self):
        self.find_element(*self.setting_Audio).click()
        self.driver.keyevent(23)
        self.find_element(*self.balance_layout).click()

    # 获取audio界面Balance值对象
    def balance_switch_click(self):
        el = self.find_element(*self.balance_switch)
        print(el.text)
        return el.text

    # setting界面->audio界面->audio_mode界面
    def audio_mode_click(self):
        self.find_element(*self.setting_Audio).click()
        self.driver.keyevent(23)
        for i in range(6):
            self.driver.keyevent(20)
        sleep(1)
        try:
            self.find_element(*self.audio_mode_layout).click()
        except:
            self.find_element(*self.audio_mode_layout).click()
        else:
            self.driver.keyevent(23)

    # 取值次数1~7，取值范围21(左) or 22(右)
    def value_switch(self):
        a = randint(1, 7)
        b = choice(['21', '22'])
        for i in range(a):
            self.driver.keyevent(eval(b))

    # 获取audio_mode界面customize和eq0值对象
    def audio_mode_name_jude(self):
        el = self.find_element(*self.audio_mode_name)
        el1 = self.find_element(*self.eq0_value)
        return el.text, el1.text

    # 回到home界面长按电源键重启
    def restart(self):
        self.driver.keyevent(3)
        self.driver.long_press_keycode(26)
        self.find_element(*self.restart_button).click()

    # 重启后根据select返回对应的对象(audio界面Balance值对象&audio_mode界面customize和eq0值对象)
    @retry(tries=2, delay=75)
    def restart_judge(self, select):
        if self.count == 0:
            self.count += 1
            self.restart()
        if self.count == 1:
            driver = webdriver.Remote("http://localhost:4723/wd/hub", CAPS1)
            driver.implicitly_wait(10)
            self.driver = driver
            driver.start_activity('com.eswin.tv.settings', '.home.HomeActivity')
            if select == 'BL':
                self.balance_layout_click()
                result2 = self.balance_switch_click()
                return result2
            elif select == 'EQ':
                self.audio_mode_click()
                result2 = self.audio_mode_name_jude()
                return result2
