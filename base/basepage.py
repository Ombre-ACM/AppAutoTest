import time
from appium import webdriver
from config.log import get_log

log = get_log()


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(15)

    def locate(self, loc):
        return self.driver.find_element(*loc)

    def input(self, loc, value):
        try:
            log.info('正在输入内容{}，输入框为{}'.format(value, loc))
            self.locate(loc).send_keys(value)
        except Exception as e:
            log.error('输入内容失败{}'.format(e))

    def click(self, loc):
        try:
            log.info('正在点击{}'.format(loc))
            self.locate(loc).click()
        except Exception as e:
            log.error('点击失败{}'.format(e))

    def sleep(self, txt):
        log.info('正在强制等待 {}秒'.format(txt))
        time.sleep(int(txt))

    def quit(self):
        log.info('正在关闭')
        self.driver.quit()

    # 通过比例滑屏
    def swipe(self, start_x, start_y, end_x, end_y, duration=1000):
        try:
            log.info('正在从屏幕坐标比例{}滑屏到{}'.format((start_x, start_y), (end_x, end_y)))

            size = self.driver.get_window_size()
            x = size['width']
            y = size['height']

            self.driver.swipe(
                     start_x=x*start_x,
                     start_y=y*start_y,
                     end_x=x*end_x,
                     end_y=y*end_y,
                     duration=duration)
        except Exception as e:
            log.error('滑屏失败{}'.format(e))

    def tap(self, tap_x, tap_y):
        try:
            log.info('正在点击坐标{}'.format((tap_x, tap_y)))

            rel_x = tap_x / 1080
            rel_y = tap_y / 2034

            x = self.driver.get_window_size()['width']
            y = self.driver.get_window_size()['height']
            #  强制等待
            time.sleep(2)
            self.driver.tap([(rel_x * x, rel_y * y)])

        except Exception as e:
            log.error('点击坐标失败{}'.format(e))
