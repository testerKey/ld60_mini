import pytest
import sys
import os
from page.videopage import VideoPage
from page.musicpage import MusicPage
from os.path import dirname, abspath

BASE_PATH = dirname(dirname(abspath(__file__)))
sys.path.append(BASE_PATH)


class TestMusicplayback:

    def test_sanity_23(self, driver):
        page = MusicPage(driver)
        driver.start_activity("com.eswin.tv.filebrowser", ".home.HomePageActivity")
        page.music_page_switch()
        page.click_music_23()
        result = page.playback_music(*page.music_23_name)
        assert result is True

    def test_sanity_24(self, driver):
        page = MusicPage(driver)
        page.click_music_24()
        result = page.playback_music(*page.music_24_name)
        assert result is True

    def test_sanity_25(self, driver):
        page = MusicPage(driver)
        page.click_music_25()
        result = page.playback_music(*page.music_25_name)
        assert result is True

    def test_sanity_26(self, driver):
        page = MusicPage(driver)
        page.click_music_26()
        result = page.playback_music(*page.music_26_name)
        assert result is True

    def test_sanity_27(self, driver):
        page = MusicPage(driver)
        page.click_music_27()
        result = page.playback_music(*page.music_27_name)
        assert result is True

    def test_sanity_28(self, driver):
        page = MusicPage(driver)
        page.click_music_28()
        result = page.playback_music(*page.music_28_name)
        assert result is True

    def test_sanity_29(self, driver):
        page = VideoPage(driver)
        driver.start_activity("com.eswin.tv.filebrowser", ".home.HomePageActivity")
        page.video_page_switch()
        page.click_video_29()
        result = page.playback_video(*page.video_29_name)
        assert result is True


if __name__ == '__main__':
    pytest.main(['-v', '-s'])
