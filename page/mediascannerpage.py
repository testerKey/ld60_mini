from selenium.webdriver.common.by import By
import sys
import os
from page.basepage import BasePage
from os.path import dirname
BASE_PATH = dirname(dirname(__file__))
sys.path.append(BASE_PATH)

class ScannerPage(BasePage):
    video_page = (By.XPATH, "//android.widget.TextView[contains(@text,'Video')]")
    picture_page = (By.XPATH, "//android.widget.TextView[contains(@text,'Picture')]")
    music_page = (By.XPATH, "//android.widget.TextView[contains(@text,'Music')]")
    picture_format = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView/\
                                android.widget.FrameLayout[1]")
    picture_elements = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView/\
                                 android.widget.FrameLayout")
    # picture_elements = (By.ID, "//com.eswin.tv.filebrowser:id/file_name")
    video_elements = (By.ID, "com.eswin.tv.filebrowser:id/videoitem_name")
    music_elements = (By.ID, "com.eswin.tv.filebrowser:id/videoitem_name")

    def video_page_switch(self):
        self.driver.keyevent(22)

    def music_page_switch(self):
        for i in range(3):
            self.driver.keyevent(22)

    def picture_page_switch(self):
        for i in range(2):
            self.driver.keyevent(22)

    def picture_format_click(self):
        self.find_element(*self.picture_format).click()
        self.driver.keyevent(23)

    def videoscan(self):
        ex_list = ['mkv', 'asf', 'wmv', 'avi', 'rm', 'rmvb', 'mp4', 'mov', '3gp', '3g2', 'mj2', 'm4v', 'm4b', 'f4v',
                   'ismv', 'ts', 'm2t', 'm2ts', 'mts', 'vob', 'mpg', 'mpeg', 'dvd', 'flv']
        findresult = []
        for i in range(10):
            self.driver.keyevent(20)
            filelist = self.find_elements(*self.video_elements)
            for j in range(len(filelist)):
                text = filelist[j].text
                extension = (((os.path.splitext(text))[1]).split('.', 1))[1]
                try:
                    ex_list.remove(extension)
                    findresult.append(extension)
                except:
                    pass
        if len(ex_list) == 0:
            return True
        else:
            print("未能扫出的video格式:")
            print(ex_list)
            print("已扫出的video格式:")
            print(findresult)
            return True

    def musicscan(self):
        ex_list = ['wav', 'ogg', 'oga', 'mp1', 'mp2', 'mp3', 'flac', 'ape', 'apl', 'mac', 'aac', 'amr', 'mka', 'wma', 'ra', 'm4a', 'isma']
        findresult = []
        for i in range(5):
            self.driver.keyevent(20)
            filelist = self.find_elements(*self.music_elements)
            for j in range(len(filelist)):
                text = filelist[j].text
                extension = (((os.path.splitext(text))[1]).split('.', 1))[1]
                try:
                    ex_list.remove(extension)
                    findresult.append(extension)
                except:
                    pass
        if len(ex_list) == 0:
            return True
        else:
            print("未能扫出的music格式:")
            print(ex_list)
            print("已扫出的music格式:")
            print(findresult)
            return True

    def picturescan(self):
        ex_list = ['jpeg', 'png', 'bmp', 'gif', 'webp', 'heif', 'jpg']
        filelist = self.find_elements(*self.picture_elements)
        if len(ex_list) == len(filelist):
            print(len(filelist))
            return True
        else:
            print("未能扫出的picture格式:")
            print(ex_list)
            return False
