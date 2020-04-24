#主运行

from config.Conf import ConfigYaml
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


if __name__ == '__main__':

    # report_path = Conf.get_report_path()+os.sep+"result"
    # report_html_path = Conf.get_report_path()+os.sep+"html"
    # print(report_path)
    # pytest.main(["-s","--alluredir",report_path])
    # #Base.send_mail()

    #pytest运行前会提前运行pytest.ini文件的内容; 运行文件test_excel_case.py;alluredir pytest报告生成路径;后面更路径
    # 运行testcase目录下所有test开头的方法

    pytest.main(["-s","testcase","--alluredir",report_path])
    Base.allure_report(report_path,report_html_path)
    Base.send_mail(content=report_path,title="测试自动发送邮件")
