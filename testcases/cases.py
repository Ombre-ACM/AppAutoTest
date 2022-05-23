import unittest
from appium import webdriver
from common.data_util import readYaml
from pageobjects.brand_page import BrandPage
from pageobjects.buy_page import BuyPage
from pageobjects.car_page import CarPage
from pageobjects.changecity_page import ChangeCityPage
from pageobjects.init_page import InitPage
from pageobjects.search_page import SearchPage
from pageobjects.sell_page import SellPage
from ddt import ddt, data, unpack, file_data
from HTMLTestRunner import HTMLTestRunner


class TestCase(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls) -> None:
        data = readYaml('../config/config.yaml')
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', data['desired_caps'])
        cls.ip = InitPage(cls.driver)
        cls.sp = SearchPage(cls.driver)
        cls.ccp = ChangeCityPage(cls.driver)
        cls.bp = BrandPage(cls.driver)
        cls.bp2 = BuyPage(cls.driver)
        cls.sp2 = SellPage(cls.driver)
        cls.cp = CarPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_001_init(self):
        self.ip.initial()

    def test_002_search(self):
        self.sp.search()

    def test_003_change(self):
        self.ccp.change()

    def test_004_brand(self):
        self.bp.brand_click()

    def test_005_buy(self):
        self.bp2.buy()

    def test_006_sell(self):
        self.sp2.sell()

    def test_007_car(self):
        self.cp.car()


if __name__ == '__main__':
    # unittest.main()

    testunit = unittest.TestSuite()
    testunit.addTest(TestCase("test_001_init"))
    testunit.addTest(TestCase("test_002_search"))
    testunit.addTest(TestCase("test_003_change"))
    testunit.addTest(TestCase("test_004_brand"))
    testunit.addTest(TestCase("test_005_buy"))
    testunit.addTest(TestCase("test_006_sell"))
    testunit.addTest(TestCase("test_007_car"))

    fp = open('../result/result.html', 'wb')
    runner = HTMLTestRunner(stream=fp, title='瓜子二手车APP测试报告', description='用例执行情况')
    runner.run(testunit)  # 执行测试用例
    fp.close()
