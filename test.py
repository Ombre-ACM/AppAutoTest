import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# 设置终端参数项
desired_caps = {
    "platformName": "Android",
    "platformVersion": "8.1.0",
    "deviceName": "b1c9cae3",
    "appPackage": "com.ganji.android.haoche_c",
    "appActivity": "com.ganji.android.haoche_c.ui.main.MainActivity",
    "noRest": True}

# 模拟器/真机 必须能被电脑识别
# 启动appium server
# 发送指令到appium server
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(20)

# 同意隐私说明
el_accept = driver.find_element(AppiumBy.ID, 'com.ganji.android.haoche_c:id/btn_confirm')
el_accept.click()

# 取消登录
el_x = driver.find_element(AppiumBy.ID, 'com.ganji.android.haoche_c:id/close')
el_x.click()

# 确认取消登录
el_cancle = driver.find_element(AppiumBy.ID, 'com.ganji.android.haoche_c:id/tv_cancel')
el_cancle.click()

# 关闭弹出权益广告
el_cancle2 = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="app"]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.view.View[1]')
el_cancle2.click()

rel_a1 = 450/1080
rel_b1 = 280/2034

x = driver.get_window_size()['width']
y = driver.get_window_size()['height']
#  强制等待
time.sleep(2)
driver.tap([(rel_a1 * x, rel_b1 * y)])
print(x, y)

el_search = driver.find_element(AppiumBy.ID, 'com.ganji.android.haoche_c:id/edit_text')
el_search.send_keys('大众')

el_search2 = driver.find_element(AppiumBy.ID, 'com.ganji.android.haoche_c:id/search_text')
el_search2.click()



