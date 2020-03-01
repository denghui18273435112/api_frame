import os
from utils.YamlUtil import YamlReaber

current =os.path.abspath(__file__)  #当前文件的路径
BASE_DIR = os.path.dirname(os.path.dirname(current))    # 当前项目的绝对路径
_config_path = BASE_DIR +os.sep+"config"    #定义config的路径
_config_file = _config_path +os.sep+"conf.yaml" #定义conf.yaml的路径
_log_path = BASE_DIR +os.sep+"logs" #定义log文件生产路径

def get_config_path():
    return  _config_path

def get_config_file():
    return  _config_file

def get_log_path():
    """
    获取log文件路径
    :return:
    """
    return _log_path


#读取配置文件
class ConfigYaml:
    #创建类；初始化yaml读取配置文件；
    def __init__(self):
        self.config = YamlReaber(get_config_file()).data()
        self.config_all = YamlReaber(get_config_file()).data_all()
    #定义需要的方法
    def get_conf_url(self):
        return self.config["BASE"]["test"]["url"]

    def get_conf_url_all(self):
        return self.config_all["BASE"]["test"]["url"]


    def get_conf_log(self):
        """
        ；获取日志级别
        :return:
        """
        return self.config["BASE"]["LOG"]["log_level"]

    def get_conf_log_extensiong(self):
        """
        ；获取文件的扩展名
        :return:
        """
        return self.config["BASE"]["LOG"]["log_extensiong"]


if __name__ == '__main__':

    print(ConfigYaml().get_conf_url())
    #print(ConfigYaml().get_conf_url_all())
    print(ConfigYaml().get_conf_log())
    print(ConfigYaml().get_conf_log_extensiong())
