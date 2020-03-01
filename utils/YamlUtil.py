# 封装读取yaml文件的方法
#  YamlUtil.py
import  os
import yaml

class YamlReaber:
    #先初始化
    def __init__(self,yamlf):
        if os.path.exists(yamlf):
            self.yamlf =yamlf
        else:
            raise FileNotFoundError("文件不存在")
        self._data = None
        self._data_all = None

    #  #当个文档
    def data(self):
        if not self._data:
            with open(self.yamlf,"rb") as f:
                self._data = yaml.safe_load(f)
            return  self._data

    # 多个文档
    def data_all(self):
        if not self._data_all:
            with open(self.yamlf,"rb") as f:
                self._data_all = list(yaml.safe_load_all(f))
            return  self._data_all