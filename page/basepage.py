from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#temp

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *loc):
        try:
            # WebDriverWait(self.driver, 10, 0.5).until(EC.invisibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            print('页面未找到元素%s' % loc)

    def find_elements(self, *loc):
        try:
            # WebDriverWait(self.driver, 10, 0.5).until(EC.invisibility_of_element_located(loc))
            return self.driver.find_elements(*loc)
        except:
            print('页面未找到元素%s' % loc)

    def send_keys(self, loc, value, clear_first=True, click_first=True):
        try:
            loc = getattr(self, '_%s' % loc)
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            print('%s页面中未找到%s元素' % (self, loc))

    def is_toast_exist(self, text):
        ''' is toast exist, return True or False
                :Agrs:
                 - driver - 传driver
                 - text   - 页面上看到的文本内容
                 - timeout - 最大超时时间，默认30s
                 - poll_frequency  - 间隔查询时间，默认0.5s查询一次
                :Usage:
                 is_toast_exist(driver, "看到的内容")
        '''
        try:
            toast_loc = (By.XPATH, ".//*[contains(@text,'%s')]" % text)
            WebDriverWait(self.driver, 10, 0.01).until(EC.presence_of_element_located(toast_loc))
            return True
        except Exception as e:
            print(e)

    def keyboard_hide(self, driver):
        try:
            self.driver.hide_keyboard()
        except:
            print('no keyboard')
        else:
            print('hide OK')
