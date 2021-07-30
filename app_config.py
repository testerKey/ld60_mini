import pytest
import sys
from page.videopage import VideoPage
from os.path import dirname, abspath
BASE_PATH = dirname(dirname(abspath(__file__)))
sys.path.append(BASE_PATH)

CAPS = {

    "deviceName": '1234567890',
    #"automationName": 'UiAutomator2',
    "platformName": 'Android',
    "platformVersion": '11',
    "appPackage": 'com.eswin.tv.launcher.lite',
    "appActivity": '.ui.activity.HomeActivity',
    'newCommandTimeout': '2000',
    "noReset": True,
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    }

CAPS1 = {

    "deviceName": '1234567890',
    #"automationName": 'UiAutomator2',
    "platformName": 'Android',
    "platformVersion": '11',
    'newCommandTimeout': '2000',
    "noReset": True,
    "unicodeKeyboard": True,
    "resetKeyboard": True,
    }