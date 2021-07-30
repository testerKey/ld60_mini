import sys
import os
import pytest
from appium import webdriver
from os.path import dirname
from app_config import CAPS1, CAPS
from selenium.webdriver.common.by import By
from time import sleep
from page.wifipage import WifiPage
BASE_PATH = dirname(dirname(__file__))
sys.path.append(BASE_PATH)


class TestWifi:

    def test_sanity_48(self, driver):
        page = WifiPage(driver)
        page.connect_wifi()
        open_result = page.network_check_all()
        page.install_apk(page.iqiyi_path)
        page.switch_iqiyi()
        open_result.append(page.playback_yh())
        page.close_wifi()
        close_result = page.network_check_all()
        page.disconnect_wifi()
        assert False not in open_result and True not in close_result

    def test_sanity_49(self, driver):
        page = WifiPage(driver)
        page.connect_wifi()
        open_result = page.network_check_all()
        page.switch_iqiyi_sec()
        open_result.append(page.playback_yh_sec())
        page.restart_judge()
        open_result.append(page.network_check_all())
        page.switch_iqiyi_sec()
        open_result.append(page.playback_yh_sec())
        page.disconnect_wifi()
        page.uinstall_yh()
        assert False not in open_result
    #
    # #  连接HF02,network界面检查HF02连接状态
    # def test_function_01_connect_hf02(self, driver):
    #     driver.start_activity("com.eswin.tv.settings", ".home.HomeActivity")
    #     page = WifiPage(driver)
    #     page.wireless_click()
    #     page.connect_wifi()
    #     result = page.hf02_check()
    #     return result
    #
    # # detection界面检查HF02连接状态
    # def test_function_02_detection_hf02(self, driver):
    #     driver.start_activity("com.eswin.tv.settings", ".home.HomeActivity")
    #     page = WifiPage(driver)
    #     # page.wireless_click()
    #     # result = page.hf02_check()
    #     page.detection_click()
    #     result = page.detection_result_check()
    #     assert result
    #
    # # 检查是否能连接baidu
    # def test_function_03_baidu_hf02(self, driver):
    #     page = WifiPage(driver)
    #     test_server = ('www.baidu.com', 443)
    #     result = page.isNetOK(test_server)
    #     assert result
    #
    # # 重启后network界面检查HF02连接状态
    # def test_function_04_restart_hf02(self, driver):
    #     driver.start_activity("com.eswin.tv.settings", ".home.HomeActivity")
    #     page = WifiPage(driver)
    #     result = page.restart_judge()
    #     assert result
    #
    # # 断开hf02
    # def test_function_05_disconnect_hf02(self, driver):
    #     # driver = webdriver.Remote("http://localhost:4723/wd/hub", CAPS)
    #     # driver.implicitly_wait(10)
    #     driver.start_activity("com.eswin.tv.settings", ".home.HomeActivity")
    #     page = WifiPage(driver)
    #     page.wireless_click()
    #     page.disconnect_hf02()
    #     result = page.hf02_check()
    #     # driver.quit()
    #     if not result:
    #         print('wifi 未连接')
    #     assert not result
    #


if __name__ == '__main__':
    pytest.main(['-v', '-s'])
