# coding=gbk
import allure


class Test_dream(object):
    @allure.step(title="��һ������")
    def test_001_class(self):
        allure.attach('���ǲ��Բ���001������~~', "��һ��")
        assert False

    # ��һ�����������ӣ�Ϊ�˸��õ�˵��
    @allure.testcase("http://www.baidu.com/test_001")
    # ��һ��bug����
    @allure.issue("http://www.163.com")
    @allure.step(title="�ڶ�������")
    @allure.severity("TRIVIAL")
    def test_002_class(self):
        allure.attach('���ǲ��Բ���001������~~', "��һ��")
        assert True

