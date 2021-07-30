# coding:utf-8
import pytest
from page.startpage import StartPage
import sys
from os.path import dirname
from appium import webdriver
from app_config import CAPS, CAPS1

BASE_PATH = dirname(dirname(__file__))
sys.path.append(BASE_PATH)


class TestKernel:

    def test_sanity_2(self, driver):
        result = False
        for i in range(1):
            page = StartPage(driver)
            result = page.restart_judge()
        assert result is True

    def test_sanity_8(self, driver):
        driver = webdriver.Remote("http://localhost:4723/wd/hub", CAPS1)
        driver.implicitly_wait(10)
        driver.start_activity('com.eswin.tv.settings', '.home.HomeActivity')
        page = StartPage(driver)
        page.setting_About_click()
        page.setting_System_Info_click()
        result = page.setting_System_Version_judge()
        assert result is True

    # @pytest.mark.skip
    # def test_sanity_3(self, driver):
    #     page = StartPage(driver)
    #     result = page.get_advertising(driver)
    #     assert result is True
    #
    # @pytest.mark.skip
    # def test_sanity_53(self, driver):
    #     page = StartPage(driver)
    #     result = page.get_advertising(driver)
    #     assert result is True


if __name__ == '__main__':
    pytest.main(['-v', '-s'])
