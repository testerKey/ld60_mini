import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root"
)


# import time
#
# now = time.time()
# result = '{}'.format(time.strftime('%d %b %X', time.localtime(now)))
# print(result)
####
# 21 Jul 15:33:58
####

# import socket
# from time import sleep
#
#
# def isNetOK(testserver):
#     s = socket.socket()
#     s.settimeout(3)
#     try:
#         status = s.connect_ex(testserver)
#         if status == 0:
#             s.close()
#             return True
#         else:
#             return False
#     except Exception as e:
#         return False
#
#
# def isNetChainOK(testserver=('www.baidu.com', 443)):
#     isOK = isNetOK(testserver)
#     return isOK
#
# def main():
#     chinanet = isNetChainOK()
#     print(chinanet)
#
#
# if __name__ == '__main__':
#     main()
#     sleep(10)

# from appium import webdriver
# import cv2
# from selenium.webdriver.common.by import By
# import sys
# from time import sleep
# from page.basepage import BasePage
# import time
# import os
# from os.path import dirname
# BASE_PATH = dirname(dirname(__file__))
# sys.path.append(BASE_PATH)

# desired_caps = {"platformName": "Android",
#                 "deviceName": "1234567890",
#                 "platformVersion": "11"
#             }
#
# driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
# sleep(10)
# driver.keyevent(3) #home键
#
# settingpath = "//android.widget.FrameLayout[5]/android.widget.LinearLayout/android.widget.ImageView" #HOME->setting
# driver.find_element_by_xpath(settingpath).click()
# sleep(5)
# driver.keyevent(23)
#
# cur_time = time.strftime('%Y-%m-%d_%H_%M_%S')
# screen_save_path = os.path.dirname(os.path.abspath('.')) + '\\screenshot\\' + cur_time + '.png'
# driver.get_screenshot_as_file(screen_save_path)

# connectpath = "//android.view.ViewGroup[1]/android.widget.ImageView" #setting->connection setting
# driver.find_element_by_xpath(connectpath).click()
# sleep(5)
# driver.keyevent(23)
# sleep(5)
#
# #下面建立wifi步骤只有在ESWIN-HF未连接状态可执行，wifi已建立后元素有变化
# # wirelessid = "com.eswin.tv.settings:id/tv_wifi" #connection setting->wireless network
# # driver.find_element_by_id(wirelessid).click()
# # driver.keyevent(23)
# # sleep(5)
#
# # eswinhfpath = "//*[@test = ESWIN-HF]" #wireless network->ESWIN-HF
# eswinhfpath = "//android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.TextView" #wireless network->ESWIN-HF
# driver.find_element_by_xpath(eswinhfpath).click()
# sleep(5)
# driver.keyevent(23)
#
# #下面建立wifi步骤只有在ESWIN-HF未连接状态可执行，wifi已建立后元素有变化
# # passwordid = "com.eswin.tv.settings:id/et_info" #ESWIN-HF->password
# # driver.find_element_by_id(passwordid).send_keys('Eswin888888')
# # sleep(5)
# # driver.keyevent(66)
# sleep(5)
# # driver.keyevent(4) #返回键
# driver.keyevent(3) #home键,注意：返回Home界面后下次再进入setting时还是这个界面
# sleep(5)
# driver.quit()



