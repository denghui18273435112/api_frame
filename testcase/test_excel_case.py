from config.Conf import ConfigYaml
import pprint
from config import Conf
import os
from common.ExcelData import Data
from utils.logUtil import my_log
from common import ExcelConfig
from utils.RequestsUtil import Request
import json
import pytest
from common import Base
from utils.AssertUitl import AssertUitl
import allure
from datetime import datetime

#1、初始化信息
#1）.初始化测试用例文件
case_file = os.path.join(Conf.get_data_path(),ConfigYaml().get_excel_file())
#2）.测试用例sheet名称
sheet_name = ConfigYaml().get_excel_sheet()
#3）.获取运行测试用例列表
data_init = Data(case_file,sheet_name)
run_list = data_init.get_run_data()

#4）.日志
log = my_log()
#初始化dataconfig
data_key = ExcelConfig.DataConfig
#2、测试用例方法，参数化运行
#一个用例的执行


report_path = Conf.get_report_path()+os.sep+"result"
report_html_path = Conf.get_report_path()+os.sep+"html"



class TestExcel:
    #1、增加Pyest
    #2、修改方法参数
    #3、重构函数内容
    #4、pytest.main

    def run_api(self,url,method,params=None,header=None,cookie=None):
        """
        发送请求api
        :return:
        """
        # 2）.接口请求
        request = Request()
        # params 转义json
        # 验证params有没有内容
        if len(str(params).strip()) is not 0:
            params = json.loads(params)
        # method post/get
        if str(method).lower() == "get":
            # 2.增加Headers
            res = request.get(url, json=params, headers=header, cookies=cookie)
        elif str(method).lower() == "post":
            res = request.post(url, json=params, headers=header, cookies=cookie)
        else:
            my_log().error("错误请求method: %s" % method)
        return res

    def run_pre(self,pre_case):
        #初始化数据
        pass
        url = ConfigYaml().get_conf_url()+pre_case[data_key.url]
        method = pre_case[data_key.method]
        params = pre_case[data_key.params]
        headers = pre_case[data_key.headers]
        cookies = pre_case[data_key.cookies]

        # 1.判断headers是否存在，json转义，无需
        # if headers:
        #     header = json.loads(headers)
        # else:
        #     header = headers
        header = Base.json_parse(headers)
        # 3.增加cookies
        # if cookies:
        #     cookie = json.loads(cookies)
        # else:
        #     cookie = cookies
        cookie = Base.json_parse(cookies)
        res = self.run_api(url,method,params,header)
        #print("前置用例执行：%s"%res)
        return res

#1）.初始化信息，url,data


    # 1、增加Pyest
    @pytest.mark.parametrize("case",run_list)
    # 2、修改方法参数
    def test_run(self,case):

        # 3、重构函数内容
        #data_key = ExcelConfig.DataConfig
        # run_list第1个用例，用例，key获取values
        #获取表格上字段的信息
        url = ConfigYaml().get_conf_url()+case[data_key.url]
        case_id = case[data_key.case_id]
        case_model = case[data_key.case_model]
        case_name = case[data_key.case_name]
        pre_exec = case[data_key.pre_exec]
        method = case[data_key.method]
        params_type = case[data_key.params_type]
        params = case[data_key.params]
        expect_result = case[data_key.expect_result]
        headers = case[data_key.headers]
        cookies =case[data_key.cookies]
        code = case[data_key.code]
        db_verify = case[data_key.db_verify]



        # 先检查一行中是否有前置条件，如果有先执行
        if pre_exec:
            pre_case = data_init.get_case_pre(pre_exec)
            print("\n 当前执行的用例编号:{};当前用例的前置条件,执行的用例编号:{}".format(case_id,pre_exec))
            pre_res = self.run_pre(pre_case)
            headers,cookies = self.get_correlation(headers,cookies,pre_res)
        res = self.run_api(url, method, params, Base.json_parse(headers),Base.json_parse(cookies))
        print("当前前置条件所执行的返回结果:{}".format(res))



        #allure报告
        allure.dynamic.feature(sheet_name)
        allure.dynamic.story(case_model)
        allure.dynamic.title(case_id+case_name)
        desc = "<font color='red'>当前执行时间: </font> {}<Br/>" \
                "<font color='red'>请求URL: </font> {}<Br/>" \
               "<font color='red'>请求类型: </font>{}<Br/>" \
                "<font color='red'>期望状态码: </font>{}<Br/>" \
                "<font color='red'>实际状态码: </font>{}<Br/>" \
               "<font color='red'>期望结果: </font>{}<Br/>" \
               "<font color='red'>实际结果: </font>{}".format(
                                    str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
                                    url,method,code,pprint.pformat(res["code"]),
                                    pprint.pformat(eval(expect_result)),
                                    pprint.pformat(res["body"]))
        allure.dynamic.description(desc)


        #断言 code、字段对比、数据对比
        AssertUitl().assert_code(int(res["code"]),int(code))
        AssertUitl().assert_int_body_dict(eval(expect_result),res ["body"])
        Base.assert_db(res["body"],db_verify)


    def get_correlation(self,headers,cookies,pre_res):
        """
        关联
        :param headers:
        :param cookies:
        :param pre_res:
        :return:
        """
        #验证是否有关联
        headers_para,cookies_para = Base.params_find(headers,cookies)
        #有关联，执行前置用例，获取结果
        if len(headers_para):
            headers_data = pre_res["body"][headers_para[0]]
        #结果替换
            headers = Base.res_sub(headers,headers_data)
        if len(cookies_para):
            cookies_data = pre_res["body"][cookies_para[0]]
            # 结果替换
            cookies = Base.res_sub(headers, cookies_data)
        return headers,cookies


if __name__ == '__main__':
    #pytest运行前会提前运行pytest.ini文件的内容; 运行文件test_excel_case.py;alluredir pytest报告生成路径;后面更路径
    pytest.main(["-s","test_excel_case.py","--alluredir",report_path])
    Base.allure_report(report_path,report_html_path)
    Base.send_mail(content=report_path,title="测试自动发送邮件")




