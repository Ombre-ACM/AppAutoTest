from appium.webdriver.common.appiumby import AppiumBy
from base.basepage import BasePage


class SearchPage(BasePage):

    # 需要的元素
    tap_cor = (450, 280)
    el_search_edit = (AppiumBy.ID, 'com.ganji.android.haoche_c:id/edit_text')
    el_search_box = (AppiumBy.ID, 'com.ganji.android.haoche_c:id/search_text')
    el_home = (AppiumBy.ID, 'com.ganji.android.haoche_c:id/radio_home')

    el_x = (AppiumBy.ID, 'com.ganji.android.haoche_c:id/tips_close')

    # 业务流程
    def search(self):
        self.tap(*self.tap_cor)
        self.input(self.el_search_edit, '不存在的车')
        self.click(self.el_search_box)
        self.sleep(2)
        self.click(self.el_x)
        self.click(self.el_home)

        self.tap(*self.tap_cor)
        self.input(self.el_search_edit, '丰田')
        self.click(self.el_search_box)
        self.sleep(2)
        self.click(self.el_home)

        self.tap(*self.tap_cor)
        self.input(self.el_search_edit, '福特')
        self.click(self.el_search_box)
        self.sleep(2)
        self.click(self.el_home)


