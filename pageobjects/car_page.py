from appium.webdriver.common.appiumby import AppiumBy
from base.basepage import BasePage


class CarPage(BasePage):

    # 需要的元素
    el_buy = (AppiumBy.ID, 'com.ganji.android.haoche_c:id/radio_buy')
    el_car = (AppiumBy.ID, 'com.ganji.android.haoche_c:id/pic_rl')

    el_buynow = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("立即订购")')

    el_login_dismiss = (AppiumBy.ID, 'com.ganji.android.haoche_c:id/close')
    el_confirm = (AppiumBy.ID, 'com.ganji.android.haoche_c:id/tv_cancel')

    def car(self):
        self.click(self.el_buy)
        self.click(self.el_car)
        self.sleep(2)

        for i in range(0, 15):
            self.swipe(0.8, 0.9, 0.8, 0.2, 500)

        self.click(self.el_buynow)

        self.click(self.el_login_dismiss)
        self.click(self.el_confirm)
