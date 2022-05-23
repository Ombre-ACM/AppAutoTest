from appium.webdriver.common.appiumby import AppiumBy
from base.basepage import BasePage


class BrandPage(BasePage):

    # 需要的元素
    el1 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("宝马")')
    el2 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("奔驰")')
    el3 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("路虎")')

    el_home = (AppiumBy.ID, 'com.ganji.android.haoche_c:id/radio_home')

    # 业务流程
    def brand_click(self):
        self.click(self.el1)
        self.sleep(1)
        self.click(self.el_home)

        self.click(self.el2)
        self.sleep(1)
        self.click(self.el_home)

        self.click(self.el3)
        self.sleep(1)
        self.click(self.el_home)
