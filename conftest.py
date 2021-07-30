import pytest
import os
from py.xml import html
from appium import webdriver
import sys
from time import sleep
from os.path import dirname, abspath
from config import RunConfig
from subprocess import Popen, PIPE, STDOUT
from app_config import CAPS

BASE_PATH = dirname(abspath(__file__))
REPORT_DIR = BASE_PATH + "\\test_report\\"
sys.path.append(BASE_PATH)


@pytest.fixture(scope='class', autouse=True)
def driver():
    global driver
    os.system('start docker start appium1')
    sleep(3)
    os.system('start docker exec -it appium1 adb connect 10.11.12.19:5555')
    sleep(3)
    cmd = 'start /b docker logs -f -t  --tail=1 appium1'
    log = open('4723.log', 'w')
    Popen(cmd, shell=True, stdout=log, stderr=STDOUT)
    try:
        driver = webdriver.Remote("http://localhost:4723/wd/hub", CAPS)
    except:
        print('driver start fail')
    else:
        driver.implicitly_wait(10)
        driver.keyevent(19)
        return driver


@pytest.fixture(scope='class', autouse=True)
def driver_close():
    yield driver
    try:
        driver.quit()
    except:
        print('driver quit fail')
    else:
        # os.system('')
        print("test end")


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    用于向测试用例中添加用例的开始时间、内部注释，和失败截图等.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    report.description = description_html(item.function.__doc__)
    report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")  # 设置编码显示中文
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            case_path = report.nodeid.replace("::", "_") + ".png"
            if "[" in case_path:
                case_name = case_path.split("-")[0] + "].png"
            else:
                case_name = case_path
            # capture_screenshots(case_name)
            img_path = "image/" + case_name.split("/")[-1]
            if img_path:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % img_path
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def description_html(desc):
    """
    将用例中的描述转成HTML对象
    :param desc: 描述
    :return:
    """
    if desc is None:
        return "No case description"
    desc_ = ""
    for i in range(len(desc)):
        if i == 0:
            pass
        elif desc[i] == '\n':
            desc_ = desc_ + ";"
        else:
            desc_ = desc_ + desc[i]

    desc_lines = desc_.split(";")
    desc_html = html.html(
        html.head(
            html.meta(name="Content-Type", value="text/html; charset=latin1")),
        html.body(
            [html.p(line) for line in desc_lines]))
    return desc_html


def capture_screenshots(case_name):
    """
    配置用例失败截图路径
    :param case_name: 用例名
    :return:
    """
    global driver
    file_name = case_name.split("/")[-1]
    new_report_dir = new_report_time()
    if new_report_dir is None:
        raise RuntimeError('没有初始化测试目录')
    image_dir = os.fspath(os.path.join(REPORT_DIR, new_report_dir, "image", file_name))
    print(image_dir)
    driver.get_screenshot_as_file(image_dir)


def new_report_time():
    """
    获取最新报告的目录名（即运行时间，例如：2018_11_21_17_40_44）
    """
    files = os.listdir(REPORT_DIR)
    files.sort()
    try:
        return files[-2]
    except IndexError:
        return None


if __name__ == "__main__":
    capture_screenshots("test_dir/test_pictureplayback.png")
