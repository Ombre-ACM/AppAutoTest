from appium.webdriver.common.appiumby import AppiumBy
from base.basepage import BasePage


class InitPage(BasePage):

    # 需要的元素
    el_accept_privacy = (AppiumBy.ID, 'com.ganji.android.haoche_c:id/btn_confirm')
    el_login_dismiss = (AppiumBy.ID, 'com.ganji.android.haoche_c:id/close')
    el_confirm = (AppiumBy.ID, 'com.ganji.android.haoche_c:id/tv_cancel')
    el_ad_dissmiss = (AppiumBy.XPATH, '//*[@resource-id="app"]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.view.View[1]')

    # 业务流程
    def initial(self):
        self.click(self.el_accept_privacy)
        self.click(self.el_login_dismiss)
        self.click(self.el_confirm)
        self.click(self.el_ad_dissmiss)
