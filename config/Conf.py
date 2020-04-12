import os
import utils.YamlUtil

current =os.path.abspath(__file__)                          #当前文件的路径
BASE_DIR = os.path.dirname(os.path.dirname(current))        # 当前项目的绝对路径
_config_path = BASE_DIR +os.sep+"config"                   #定义config的路径
_config_file = _config_path +os.sep+"conf.yaml"            #定义conf.yaml的路径
_db_config_file = _config_path +os.sep+"db_conf.yaml"     #定义db_conf.yaml的路径
_log_path = BASE_DIR +os.sep+"logs"                        #定义log文件生产路径
_data_path =BASE_DIR +os.sep+"data"                        #定义data文件的路径
_report_path =BASE_DIR +os.sep+"report"                        #定义report文件的路径

def get_report_path():
    """
    :return: report文件夹的绝对路径
    """
    return  _report_path


def get_config_path():
    """
    :return: config文件夹的路径
    """
    return  _config_path

def get_db_config_cpath():
    """
    :return: db_conf.yaml 文件所在的路径
    """
    return _db_config_file

def get_config_file():
    """
    :return: conf.yaml文件所在的路径
    """
    return  _config_file

def get_data_path():
    """
    :return: data文件夹所在路径
    """
    return _data_path

def get_log_path():
    """
    :return: logs文件夹的路径
    """
    return _log_path


class ConfigYaml:
    """
    此类的主要功能获取yaml文件中的数据;
    """
    def __init__(self):
        """
        #读取配置文件
        #创建类；初始化yaml读取配置文件；
        self.config return  遍历  get_config_file方法中conf.yaml文件的所有值
        self.config_all return 遍历   get_config_file方法中conf.yaml文件的所有值
        self.db_config  return 遍历   get_config_file方法中 db_conf.yaml文件的所有值
        :return:
        """
        self.config = utils.YamlUtil.YamlReaber(get_config_file()).data()
        self.config_all = utils.YamlUtil.YamlReaber(get_config_file()).data_all()
        self.db_config = utils.YamlUtil.YamlReaber(get_db_config_cpath()).data()

    def get_report_path(self):
        """
        :return: report文件夹的绝对路径
        """
        return  _report_path


    def get_excel_file(self):# 获取
        """
        :return: 测试用例表格名称
        """
        return  self.config["BASE"]["case_file"]

    def get_excel_sheet(self):
        """
        :return: 测试用例表格sheet
        """
        return  self.config["BASE"]["case_sheet"]

    def get_conf_url(self):
        """
        :return: url地址
        """
        return self.config["test_environment"]["url"]

    def get_conf_log(self):
        """
        :return: 日志级别
        """
        return self.config["LOG"]["log_level"]

    def get_conf_log_extensiong(self):
        """
        :return: 文件的扩展名
        """
        return self.config["LOG"]["log_extensiong"]

    def get_db_conf_info(self,db_alias):
        """
        :param db_alias: 数据库的别名
        :return: 返回db_alias的所有数据
        """
        return  self.db_config[db_alias]


    def get_email_info(self):
        """
        :param  获取eamil的相关信息
        :return:
        """
        return self.config["email"]

if __name__ == '__main__':

    #pass
    #print(ConfigYaml().get_conf_url())
    #print(ConfigYaml().get_conf_log())
    #print(ConfigYaml().get_conf_log_extensiong())
    #print(ConfigYaml().get_db_conf_info("db_1"))
    # print(ConfigYaml().get_excel_file())
    #print(ConfigYaml().get_excel_sheet())
    print(ConfigYaml().get_email_info())



