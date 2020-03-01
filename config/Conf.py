import os
from utils.YamlUtil import YamlReaber

#当前文件的路径
current =os.path.abspath(__file__)
#print(current)

# 当前项目的路径
BASE_DIR = os.path.dirname(os.path.dirname(current))
#print(BASE_DIR)

#定义config的路径
_config_path = BASE_DIR +os.sep+"config"

#定义conf.yaml的路径
_config_file = _config_path +os.sep+"conf.yaml"

#定义log文件生产路径
_log_path = BASE_DIR +os.sep+"logs"

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

    def __init__(self):
        self.config = YamlReaber(get_config_file()).data()
        self.config_all = YamlReaber(get_config_file()).data_all()

    def get_conf_url(self):
        return self.config_all["BASE"]["test"]["url"]

    def get_conf_url_all(self):
        return self.config_all["BASE"]["test"]["url"]

    def get_conf_log(self):
        """
        ；获取日志级别
        :return:
        """
        return self.config_all["BASE"]["log_level"]

    def get_conf_log_extensiong(self):
        """
        ；获取文件的扩展名
        :return:
        """
        return self.config_all["BASE"]["log_extensiong"]


if __name__ == '__main__':

    #print(ConfigYaml().get_conf_url())
    print(ConfigYaml().get_conf_log())
    # print(ConfigYaml().get_conf_log_extensiong())
