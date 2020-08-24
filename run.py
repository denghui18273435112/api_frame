#主运行
import pytest
from common import Base

if __name__ == '__main__':
    #pytest运行前会提前运行pytest.ini文件的内容; 运行文件test_excel_case.py;alluredir pytest报告生成路径;后面更路径

    pytest.main(["-s","testcase","--alluredir",Base.report_path()])  # 运行testcase目录下所有test开头的方法
    Base.allure_report(Base.report_path(),Base.report_html_path())
    # Base.send_mail(content=Base.report_path(),title="测试自动发送邮件")
