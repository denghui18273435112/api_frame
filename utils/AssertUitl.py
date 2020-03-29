# coding=utf-8
from utils.logUtil import my_log
import json

#1、 定义封装方法
class AssertUitl:
    def __init__(self):
        self.log = my_log("AssertUilt")

    def assert_code(self,code,expected_code):
        """
        #预期和实际是否一致;#抛出异常；如果相等返回ture;如果不相等抛出异常

         有关于python里raise显示引发异常的方法:
        当程序出错时,python会自动触发异常,也可以通过raise显示引发异常
        一旦执行了raise语句,raise之后的语句不在执行
        如果加入了try,except,那么except里的语句会被执行
        :param code:
        :param expected_code:
        :return:
        """
        try:
            assert  int(code) == int(expected_code)
            return "两个code一致"
        except:
            self.log.error("code error; code is {0},expected_code is {1}".format(code,expected_code))
            raise

    def assert_body(self,body,expected_body):
        """
        验证返回结果内容相等
        :param body:
        :param expected_body:
        :return:
        """
        try:
            assert  body == expected_body
            return  "两个body相同"
        except:
            self.log.error("body error; body is {0},expected_body is {1}".format(body,expected_body))
            raise

    def assert_int_body(self,body,expected_body):
        """
        验证返回结果是否包含
        :param body:
        :param expected_body:
        :return:
        """
        try:
            body = json.dumps(body)
            assert  expected_body in body
            return  True
        except:
            self.log.error("不包含或者body错误; body is {0},expected_body is {1}".format(body,expected_body))
            raise