from appium.webdriver.common.appiumby import AppiumBy
from base.basepage import BasePage


class ChangeCityPage(BasePage):

    # 需要的元素
    el1 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("未知")')
    el2 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("北京")')

    el3 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("北京")')
    el4 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("广州")')

    el5 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("广州")')
    el6 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("成都")')

    # 业务流程
    def change(self):
        self.click(self.el1)
        self.click(self.el2)
        self.sleep(2)

        self.click(self.el3)
        self.click(self.el4)
        self.sleep(2)

        self.click(self.el5)
        self.click(self.el6)
        self.sleep(2)


