import cv2
from selenium.webdriver.common.by import By
import sys
from time import sleep
from page.basepage import BasePage
import time
import os
from os.path import dirname
BASE_PATH = dirname(dirname(__file__))
sys.path.append(BASE_PATH)

class PicturePage(BasePage):
    picture_30 = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[3]")
    picture_31 = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[4]")
    picture_32 = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]")
    picture_31_1 = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]")
    picture_31_2 = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]")
    picture_31_3 = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[3]")
    picture_31_4 = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[4]")
    picture_31_5 = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[5]")
    picture_31_6 = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[6]")
    picture_31_7 = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[7]")
    picture_32_1 = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]")
    picture_32_2 = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]")
    picture_32_3 = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[3]")
    picture_32_4 = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[4]")
    picture_page = (By.XPATH, "//android.widget.TextView[contains(@text,'Picture')")

    def picture_page_switch(self, driver):
        for i in range(2):
            driver.keyevent(22)

    def click_picture_30(self, driver):
        self.find_element(*self.picture_30).click()  # 进入jpeg文件夹
        driver.keyevent(23)
        driver.keyevent(23)  # 只有一张图

    def click_picture_31(self, driver):
        try:
            self.find_element(*self.picture_31).click()  # 尝试进入png文件夹
        except Exception as e:
            driver.keyevent(4)  # 返回上一层
            self.find_element(*self.picture_31).click()  # 再次进入png文件夹
            driver.keyevent(23)
        else:
            driver.keyevent(23)

    def click_picture_31_1(self, driver):
        try:
            self.find_element(*self.picture_31_1).click()
        except Exception as e:
            driver.keyevent(4)
            self.find_element(*self.picture_31_1).click()
            driver.keyevent(23)
        else:
            driver.keyevent(23)

    def click_picture_31_2(self, driver):
        try:
            self.find_element(*self.picture_31_2).click()
        except Exception as e:
            driver.keyevent(4)
            self.find_element(*self.picture_31_2).click()
            driver.keyevent(23)
        else:
            driver.keyevent(23)

    def click_picture_31_3(self, driver):
        try:
            self.find_element(*self.picture_31_3).click()
        except Exception as e:
            driver.keyevent(4)
            self.find_element(*self.picture_31_3).click()
            driver.keyevent(23)
        else:
            driver.keyevent(23)

    def click_picture_31_4(self, driver):
        try:
            self.find_element(*self.picture_31_4).click()
        except Exception as e:
            driver.keyevent(4)
            self.find_element(*self.picture_31_4).click()
            driver.keyevent(23)
        else:
            driver.keyevent(23)

    def click_picture_31_5(self, driver):
        try:
            self.find_element(*self.picture_31_5).click()
        except Exception as e:
            driver.keyevent(4)
            self.find_element(*self.picture_31_5).click()
            driver.keyevent(23)
        else:
            driver.keyevent(23)

    def click_picture_31_6(self, driver):
        try:
            self.find_element(*self.picture_31_6).click()
        except Exception as e:
            driver.keyevent(4)
            self.find_element(*self.picture_31_6).click()
            driver.keyevent(23)
        else:
            driver.keyevent(23)

    def click_picture_31_7(self, driver):
        try:
            self.find_element(*self.picture_31_7).click()
        except Exception as e:
            driver.keyevent(4)
            self.find_element(*self.picture_31_7).click()
            driver.keyevent(23)
        else:
            driver.keyevent(23)

    def click_picture_32(self, driver):
        driver.keyevent(4)  # 这里元素冲突，需要退回到文件夹界面
        try:
            self.find_element(*self.picture_32).click()  # 尝试进入gif文件夹
        except Exception as e:
            driver.keyevent(4)  # 返回上一层
            self.find_element(*self.picture_32).click()  # 再次进入gif文件夹
            driver.keyevent(23)
        else:
            driver.keyevent(23)

    def click_picture_32_1(self, driver):
        try:
            self.find_element(*self.picture_32_1).click()
        except Exception as e:
            driver.keyevent(4)
            self.find_element(*self.picture_32_1).click()
            driver.keyevent(23)
        else:
            driver.keyevent(23)

    def click_picture_32_2(self, driver):
        try:
            self.find_element(*self.picture_32_2).click()
        except Exception as e:
            driver.keyevent(4)
            self.find_element(*self.picture_32_2).click()
            driver.keyevent(23)
        else:
            driver.keyevent(23)

    def click_picture_32_3(self, driver):
        try:
            self.find_element(*self.picture_32_3).click()
        except Exception as e:
            driver.keyevent(4)
            self.find_element(*self.picture_32_3).click()
            driver.keyevent(23)
        else:
            driver.keyevent(23)

    def click_picture_32_4(self, driver):
        try:
            self.find_element(*self.picture_32_4).click()
        except Exception as e:
            driver.keyevent(4)
            self.find_element(*self.picture_32_4).click()
            driver.keyevent(23)
        else:
            driver.keyevent(23)

    def average_hash(self, img):
        # 缩放为8*8
        img = cv2.resize(img, (8, 8), interpolation=cv2.INTER_CUBIC)
        # 转换为灰度图
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # s为像素和初值为0，hash_str为hash值初值为''
        s = 0
        hash_str = ''
        # 遍历累加求像素和
        for i in range(8):
            for j in range(8):
                s = s + gray[i, j]
        # 求平均灰度
        avg = s / 64
        # 灰度大于平均值为1相反为0生成图片的hash值
        for i in range(8):
            for j in range(8):
                if gray[i, j] > avg:
                    hash_str = hash_str + '1'
                else:
                    hash_str = hash_str + '0'
        return hash_str

    # 差值感知算法
    def dif_hash(self, img):
        # 缩放8*8
        img = cv2.resize(img, (9, 8), interpolation=cv2.INTER_CUBIC)
        # 转换灰度图
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        hash_str = ''
        # 每行前一个像素大于后一个像素为1，相反为0，生成哈希
        for i in range(8):
            for j in range(8):
                if gray[i, j] > gray[i, j + 1]:
                    hash_str = hash_str + '1'
                else:
                    hash_str = hash_str + '0'
        return hash_str

    def compare_hash(self, hash1, hash2):
        n = 0  # 相似度0-64
        # hash长度不同则返回-1代表传参出错
        if len(hash1) != len(hash2):
            return -1
        # 遍历判断
        for i in range(len(hash1)):
            # 不相等则n计数+1，n最终为相似度
            if hash1[i] != hash2[i]:
                n = n + 1
        return n

    def compare_images(self, driver, path_one):
        sleep(2)
        img_folder = os.fspath('C:\\screenshots') + '\\' + "screeshot" # screenshots文件夹需要提前手动创建
        screentime = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screen_save_path = img_folder + screentime + '.png'
        # cur_time = time.strftime('%Y-%m-%d_%H_%M_%S')
        # screen_save_path = os.path.dirname(os.path.abspath('.')) + '\\screenshot\\' + cur_time + '.png'
        driver.get_screenshot_as_file(screen_save_path)
        image_one = cv2.imread(path_one)
        image_two = cv2.imread(screen_save_path)
        # 均值Hash对比
        hash_one = self.average_hash(image_one)
        hash_two = self.average_hash(image_two)
        n = self.compare_hash(hash_one, hash_two)
        # 差值hash对比
        hash_two = self.dif_hash(image_two)
        hash_one = self.dif_hash(image_one)
        m = self.compare_hash(hash_one, hash_two)
        if n <= 5 and m <= 5:
            print('图片一致')
            return True
        else:
            print('均值哈希算法相似度为{}'.format(str(n)))
            print('差值哈希算法相似度为{}'.format(str(m)))
            return False

    def playback_picture(self, driver):
        for i in range(1):
            sleep(1)
            driver.keyevent(22)
            sleep(1)
            driver.keyevent(21)
            driver.keyevent(4)
            # driver.keyevent(23)
        driver.keyevent(4) # 返回thumbnail
