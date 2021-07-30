import pytest
import sys
from os.path import dirname, abspath
from page.picturepage import PicturePage

BASE_PATH = dirname(dirname(abspath(__file__)))
sys.path.append(BASE_PATH)


class TestPictureplayback:

    def test_sanity_30(self, driver):
        page = PicturePage(driver)
        driver.start_activity("com.eswin.tv.filebrowser", ".home.HomePageActivity")
        page.picture_page_switch(driver)
        page.click_picture_30(driver)
        path = 'C:\\screenshots\\screeshot20210714160931.png'  # 参照图文件路径
        result = page.compare_images(driver, path)  # 截图与参照图对比
        page.playback_picture(driver)
        assert result is True

    def test_sanity_31_1(self, driver):  # 测试第一个png图片
        page = PicturePage(driver)
        page.click_picture_31(driver)
        page.click_picture_31_1(driver)
        path = 'C:\\screenshots\\screeshot20210714171544.png'
        result = page.compare_images(driver, path)
        page.playback_picture(driver)
        assert result is True

    # def test_sanity_31_2(self, driver):
    #     page = PicturePage(driver)
    #     page.click_picture_31_2(driver)
    #     path = 'D:\\Picture\\png\\IMG_176x144_Overlay2.png'
    #     result = page.compare_images(driver, path)
    #     page.playback_picture(driver)
    #     assert result is True
    #
    # def test_sanity_31_3(self, driver):
    #     page = PicturePage(driver)
    #     page.click_picture_31_3(driver)
    #     path = 'D:\\Picture\\png\\IMG_640x480.png'
    #     result = page.compare_images(driver, path)
    #     print(result)
    #     page.playback_picture(driver)
    #     assert result is True
    #
    # def test_sanity_31_4(self, driver):
    #     page = PicturePage(driver)
    #     page.click_picture_31_4(driver)
    #     path = 'D:\\Picture\\png\\IMG_640x480_Overlay1.png'
    #     result = page.compare_images(driver, path)
    #     page.playback_picture(driver)
    #     assert result is True
    #
    # def test_sanity_31_5(self, driver):
    #     page = PicturePage(driver)
    #     page.click_picture_31_5(driver)
    #     path = 'D:\\Picture\\png\\IMG_640x480_Overlay2.png'
    #     result = page.compare_images(driver, path)
    #     page.playback_picture(driver)
    #     assert result is True
    #
    # def test_sanity_31_6(self, driver):
    #     page = PicturePage(driver)
    #     page.click_picture_31_6(driver)
    #     path = 'D:\\Picture\\png\\PNG_176x144_24bit_17.8k.png'
    #     result = page.compare_images(driver, path)
    #     page.playback_picture(driver)
    #     assert result is True
    #
    # def test_sanity_31_7(self, driver):
    #     page = PicturePage(driver)
    #     page.click_picture_31_7(driver)
    #     path = 'D:\\Picture\\png\\PNG_WVGA_800x480_24bit_671k.png'
    #     result = page.compare_images(driver, path)
    #     page.playback_picture(driver)
    #     assert result is True
    #
    # def test_sanity_32_1(self, driver):
    #     page = PicturePage(driver)
    #     page.click_picture_32(driver)
    #     page.click_picture_32_1(driver)
    #     path = 'D:\\Picture\\gif\\GIF_89a_1024x768_Static_142k.gif'
    #     result = page.compare_images(driver, path)
    #     page.playback_picture(driver)
    #     assert result is True
    #
    # def test_sanity_32_2(self, driver):
    #     page = PicturePage(driver)
    #     page.click_picture_32_2(driver)
    #     path = 'D:\\Picture\\gif\\GIF_89a_432x240_2.9M.gif'
    #     result = page.compare_images(driver, path)
    #     page.playback_picture(driver)
    #     assert result is True
    #
    # def test_sanity_32_3(self, driver):
    #     page = PicturePage(driver)
    #     page.click_picture_32_3(driver)
    #     path = 'D:\\Picture\\gif\\GIF_89a_800x352_Dynamic_3M.gif'
    #     result = page.compare_images(driver, path)
    #     page.playback_picture(driver)
    #     assert result is True
    #
    # def test_sanity_32_4(self, driver):
    #     page = PicturePage(driver)
    #     page.click_picture_32_4(driver)
    #     path = 'D:\\Picture\\gif\\IMG_640x480.gif'
    #     result = page.compare_images(driver, path)
    #     page.playback_picture(driver)
    #     assert result is True


if __name__ == '__main__':
    pytest.main(['-v', '-s'])
