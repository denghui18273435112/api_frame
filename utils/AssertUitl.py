# coding=utf-8
from utils.logUtil import my_log
import json

class AssertUitl:
    def __init__(self):
        self.my_log = my_log("AssertUilt")

    def assert_code(self,code,expected_code):
        """
        #预期和实际是否一致;#抛出异常；如果相等返回ture;如果不相等抛出异常
         有关于python里raise显示引发异常的方法:
        当程序出错时,python会自动触发异常,也可以通过raise显示引发异常
        一旦执行了raise语句,raise之后的语句不在执行
        如果加入了try,except,那么except里的语句会被执行
        :param code: 接口请求所返回的状态码
        :param expected_code: 需要对比的状态码
        :return:
        """
        try:
            assert  int(code) == int(expected_code)
            return "两个code一致"
        except:
            self.my_log.error("code error; code is {0},expected_code is {1}".format(code,expected_code))
            raise

    def assert_body(self,body,expected_body):
        """
        验证返回结果内容相等
        :param body:  接口请求所返回的body
        :param expected_body:需要对比的body
        :return:
        """
        try:
            assert  body == expected_body
            return  "两个body相同"
        except:
            self.my_log.error("body error; body is {0},expected_body is {1}".format(body,expected_body))
            raise

    def assert_int_body(self,body,expected_body):
        """
        验证返回结果是否包含
        :param body:            接口请求所返回的body
        :param expected_body:  需要对比的body
        :return:
        """
        try:
            body = json.dumps(body)
            print("验证返回结果是否包含",body)
            assert  expected_body in body
            return  True
        except:
            self.my_log.error("不包含或者body错误; 接口请求所返回的bodybody is {0}, 需要对比的bodyexpected_body is {1}".format(body,expected_body))
            raise

if __name__ == '__main__':

    a={'username': 'python', 'user_id': 1, 'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1OTI3MTg2NjIsInVzZXJuYW1lIjoicHl0aG9uIiwiZW1haWwiOiI5NTI2NzM2MzhAcXEuY29tIiwidXNlcl9pZCI6MX0.njna_85CMoCiviEfJH9ujcPotcM0mZVnCJUk_DVI4q4'}
    b={'user_id': 1}
    AssertUitl().assert_int_body(1,1)
