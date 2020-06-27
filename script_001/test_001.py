# coding=gbk
import allure


class Test_dream(object):
    @allure.step(title="第一个测试")
    def test_001_class(self):
        allure.attach('我是测试步骤001的描述~~', "试一下")
        assert False

    # 给一个用例的链接，为了更好的说明
    @allure.testcase("http://www.baidu.com/test_001")
    # 给一个bug链接
    @allure.issue("http://www.163.com")
    @allure.step(title="第二个测试")
    @allure.severity("TRIVIAL")
    def test_002_class(self):
        allure.attach('我是测试步骤001的描述~~', "试一下")
        assert True

