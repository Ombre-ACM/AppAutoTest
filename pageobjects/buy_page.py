from appium.webdriver.common.appiumby import AppiumBy
from base.basepage import BasePage


class BuyPage(BasePage):

    # 需要的元素
    el_buy = (AppiumBy.ID, 'com.ganji.android.haoche_c:id/radio_buy')

    el_clear = (AppiumBy.ID, 'com.ganji.android.haoche_c:id/reset_btn')

    el_brand = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("品牌")')
    el_brand2 = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("奥迪")')
    # 切换frame
    # el_series = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("不限车系")')

    tap_cor = (750, 600)

    el_age = (AppiumBy.ID, "com.ganji.android.haoche_c:id/ftv_license_roadHaul")
    el_submit = (AppiumBy.ID, "com.ganji.android.haoche_c:id/layout_license_roadHaul_submit")
    el_home = (AppiumBy.ID, 'com.ganji.android.haoche_c:id/radio_home')

    # 业务流程
    def buy(self):
        self.click(self.el_buy)
        self.sleep(1)
        self.click(self.el_clear)
        self.sleep(1)

        self.click(self.el_brand)
        self.sleep(1)
        self.click(self.el_brand2)
        self.sleep(1)
        self.tap(*self.tap_cor)
        self.sleep(1)

        self.click(self.el_age)
        self.sleep(1)
        self.click(self.el_submit)
        self.sleep(1)

        self.click(self.el_home)
