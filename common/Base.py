# coding=utf-8
from config.Conf import ConfigYaml
from utils.MysqlUitl import Mysql
import json
import  re
from utils.logUtil import my_log
from utils.AssertUitl import AssertUitl

p_data = '\${(.*)}\$'
log = my_log()

def init_db(db_alias='db_1'):
    """
    :param db_alias: # 默认db_1  数据库
    :return: sql的光标对象
    """
    db_info = ConfigYaml().get_db_conf_info(db_alias)
    host  = db_info["db_host"]
    user  = db_info["db_user"]
    password  = db_info["db_password"]
    database  = db_info["db_database"]
    port  = int(db_info["db_port"])
    charse  = db_info["db_charset"]
    conn =  Mysql(host,user,password,database,port,charse)
    return  conn

def json_parse(data):
    """
    转换json格式
    :param data:需要格式转译格式化字符
    :return: 转译后的数据
    不晓得有啥用
    """
      # 1.判断headers是否存在，json转义，无需
        # if headers:
        #     header = json.loads(headers)
        # else:
        #     header = headers
        #header = Base.json_parse(headers)
        # 3.增加cookies
        # if cookies:
        #     cookie = json.loads(cookies)
        # else:
        #     cookie = cookies
    return json.loads(data) if data else data

def res_find(data,pattern_data=p_data):
    """
    查询
    :param data:需要提取的原数据
    :param pattern_data: 正则表达提取格式
    :return:
    """
    pattern = re.compile(pattern_data)
    re_res = pattern.findall(data)
    return re_res

def res_sub(data,replace,pattern_data=p_data):
    """
    替换
    :param data:原内容
    :param replace: 替换内容
    :param pattern_data:正则表达提取格式
    :return: 替换后实际内容
    """
    pattern = re.compile(pattern_data)
    re_res = pattern.findall(data)
    if re_res:
        return re.sub(pattern_data,replace,data)
    return re_res

def params_find(headers,cookies):
    """
    验证请求中是否有${}$需要结果关联
    不晓得怎么用
    :param headers:
    :param cookies:
    :return:
    """
    if "${" in headers:
        headers = res_find(headers)
    if "${" in cookies:
        cookies = res_find(cookies)
    return headers,cookies

def allure_report(report_path,report_html):
    """
    生成allure 报告
    :param report_path:
    :param report_html:
    :return:
    """
    #执行命令 allure generate
    allure_cmd ="allure generate %s -o %s --clean"%(report_path,report_html)
    #subprocess.call
    log.info("报告地址")
    try:
        subprocess.call(allure_cmd,shell=True)
    except:
        log.error("执行用例失败，请检查一下测试环境相关配置")
        raise

def send_mail(report_html_path="",content="",title="测试"):
    """
    发送邮件
    :param report_html_path:
    :param content:
    :param title:
    :return:
    """
    email_info = ConfigYaml().get_email_info()
    smtp_addr = email_info["smtpserver"]
    username = email_info["username"]
    password = email_info["password"]
    recv = email_info["receiver"]
    email = SendEmail(
        smtp_addr=smtp_addr,
        username=username,
        password=password,
        recv=recv,
        title=title,
        content=content,
        file=report_html_path)
    email.send_mail()

def assert_db(db_name,result,db_verify):
    """
    数据库比较
    :param db_name:  数据库名称
    :param result:  返回的结果 body
    :param db_verify: sql语句
    :return:
    """
    assert_util =  AssertUitl()
    #sql = init_db("db_1")
    sql = init_db(db_name)
    # 2、查询sql，excel定义好的
    db_res = sql.fetchone(db_verify)

    #log.debug("数据库查询结果：{}".format(str(db_res)))
    # 3、数据库的结果与接口返回的结果验证
    # 获取数据库结果的key
    verify_list = list(dict(db_res).keys())
    # 根据key获取数据库结果，接口结果
    for line in verify_list:
        #res_line = res["body"][line]
        res_line = result[line]
        res_db_line = dict(db_res)[line]
        # 验证
        assert_util.assert_body(res_line, res_db_line)

if __name__ == '__main__':
    pass
    print(init_db("db_1"))
    print(res_find( '{"Authorization": "JWT ${token}$"}'))
    print(res_sub( '{"Authorization": "JWT ${token}$"}',"123"))
    #print(params_find())