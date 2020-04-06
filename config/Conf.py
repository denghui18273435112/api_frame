import os
from utils.YamlUtil import YamlReaber

current =os.path.abspath(__file__)  #当前文件的路径
BASE_DIR = os.path.dirname(os.path.dirname(current))    # 当前项目的绝对路径
_config_path = BASE_DIR +os.sep+"config"    #定义config的路径
_config_file = _config_path +os.sep+"conf.yaml" #定义conf.yaml的路径
_db_config_file = _config_path +os.sep+"db_conf.yaml" #定义db_conf.yaml的路径
_log_path = BASE_DIR +os.sep+"logs" #定义log文件生产路径
_data_path =BASE_DIR +os.sep+"data" #定义data文件的路径


def get_config_path():#获取config的路径
    return  _config_path

def get_db_config_cpath():#获取config的路径
    return _db_config_file

def get_config_file():#获取conf.yaml的路径
    return  _config_file

def get_data_path():#获取data文件路径
    return _data_path

def get_log_path():#获取log文件路径
    return _log_path


#读取配置文件
class ConfigYaml:
    #创建类；初始化yaml读取配置文件；
    def __init__(self):
        self.config = YamlReaber(get_config_file()).data()  # YamlReaber(get_config_file())初始化；get_config_file()返回conf.yaml的绝对路径；data()调用data方法
        self.config_all = YamlReaber(get_config_file()).data_all()  # YamlReaber(get_config_file())初始化；get_config_file()返回conf.yaml的绝对路径；data_all()调用data_all方法
        self.db_config = YamlReaber(get_db_config_cpath()).data()

    def get_conf_url(self):#获取url地址
        return self.config["test_environment"]["url"]

    def get_conf_log(self):#获取日志级别
        return self.config["LOG"]["log_level"]

    def get_conf_log_extensiong(self):#获取文件的扩展名
        return self.config["LOG"]["log_extensiong"]

    def get_db_conf_info(self,db_alias):
        '''
        根据db_alias获取名称下的数据库信息
        :param db_alias:
        :return:
        '''
        return  self.db_config[db_alias]


if __name__ == '__main__':
    #print(ConfigYaml().get_conf_url())
    #print(ConfigYaml().get_conf_log())
    #print(ConfigYaml().get_conf_log_extensiong())
    print(ConfigYaml().get_db_conf_info("db_1"))
