# coding: utf - 8
import pytest
import sys
from page.videopage import VideoPage
from os.path import dirname, abspath
BASE_PATH = dirname(dirname(abspath(__file__)))
sys.path.append(BASE_PATH)


class TestVideoplayback:

    def test_sanity_15(self, driver):
        page = VideoPage(driver)
        driver.start_activity("com.eswin.tv.filebrowser", ".home.HomePageActivity")
        page.video_page_switch()
        page.click_video_15()
        result = page.playback_video(*page.video_15_name)
        assert result is True

    def test_sanity_16(self, driver):
        page = VideoPage(driver)
        page.click_video_16()
        result = page.playback_video(*page.video_16_name)
        assert result is True

    def test_sanity_17(self, driver):
        page = VideoPage(driver)
        page.click_video_17()
        result = page.playback_video(*page.video_17_name)
        assert result is True

    def test_sanity_18(self, driver):
        page = VideoPage(driver)
        page.click_video_18()
        result = page.playback_video(*page.video_18_name)
        assert result is True

    def test_sanity_19(self, driver):
        page = VideoPage(driver)
        page.click_video_19()
        result = page.playback_video(*page.video_19_name)
        assert result is True

    def test_sanity_20(self, driver):
        page = VideoPage(driver)
        page.click_video_20()
        result = page.playback_video(*page.video_20_name)
        assert result is True

    def test_sanity_21(self, driver):
        page = VideoPage(driver)
        page.click_video_21()
        result = page.playback_video(*page.video_21_name)
        assert result is True

    def test_sanity_22(self, driver):
        page = VideoPage(driver)
        page.click_video_22()
        result = page.playback_video(*page.video_22_name)
        assert result is True


if __name__ == '__main__':
    pytest.main(['-v', '-s'])
