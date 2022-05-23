from appium.webdriver.common.appiumby import AppiumBy
from base.basepage import BasePage


class SellPage(BasePage):

    # 需要的元素
    el_sell = (AppiumBy.ID, 'com.ganji.android.haoche_c:id/radio_sell')
    el_brand = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("请选择品牌车系")')
    # el_brand2 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("大众")')
    # el_series = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("捷达")')
    # el_age = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("2019款")')
    # el_car = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("2019款 梦想版 1.4L 手动时尚型")')
    tap_cor1 = (115, 635)
    tap_cor2 = (350, 525)
    tap_cor3 = (445, 500)
    tap_cor4 = (500, 625)
    tap_cor5 = (700, 1700)
    tap_cor6 = (560, 1760)
    tap_cor7 = (425, 1200)

    el_login_dismiss = (AppiumBy.ID, 'com.ganji.android.haoche_c:id/close')
    el_confirm = (AppiumBy.ID, 'com.ganji.android.haoche_c:id/tv_cancel')

    el_home = (AppiumBy.ID, 'com.ganji.android.haoche_c:id/radio_home')

    # 业务流程
    def sell(self):
        self.click(self.el_sell)
        self.sleep(1)
        self.click(self.el_brand)
        self.sleep(1)

        self.tap(*self.tap_cor1)
        self.sleep(1)
        self.tap(*self.tap_cor2)
        self.sleep(1)
        self.tap(*self.tap_cor3)
        self.sleep(1)
        self.tap(*self.tap_cor4)
        self.sleep(1)
        self.tap(*self.tap_cor5)
        self.sleep(1)
        self.tap(*self.tap_cor6)
        self.sleep(1)
        self.tap(*self.tap_cor7)

        self.click(self.el_login_dismiss)
        self.click(self.el_confirm)
        self.click(self.el_home)
