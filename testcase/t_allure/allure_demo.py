# coding=utf-8
import pytest
import allure
#测试方法
@allure.feature("定义功能模块，往下是story-接口测试，这是一个一级标签")

class TestAllure:
    @allure.title("可以自动为用例模块，标题默认认为函数名；-测试用例标题1")
    @allure.description("测试用例的详情说明-执行测试用例1的结果是test1-标题")
    @allure.story("定义用户故事-这是一个二级标签：test1")
    @allure.severity(allure.severity_level.BLOCKER) # 定义用例的级别
    def test_1(self):
        print("test1")

    @allure.title("测试用例标题2")
    @allure.description("执行测试用例1的结果是test2")
    @allure.story("这是一个二级标签：test1")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_2(self):
        print("test2")

    @allure.title("测试用例标题3")
    @allure.description("执行测试用例1的结果是test3")
    @allure.story("这是一个二级标签：test3")
    def test_3(self):
        print("test3")

    @pytest.mark.parametrize("case",["case1","case2"])
    def test_4(self,case):
        """
        动态获取参数  allure.dynamic
        :param case:
        :return:
        """
        print(case)
        allure.dynamic.title(case)
        allure.dynamic.description(case)
        allure.dynamic.testcase(case)

if __name__ == '__main__':
    pytest.main(["allure_demo.py","r","s"])
