# 封装读取yaml文件的方法
#  YamlUtil.py
import  os
import yaml

class YamlReaber: #创建一个类

    #先初始化；文件是否存在
    def __init__(self,yamlfile):  #yamlfile 文件名
        if os.path.exists(yamlfile): #判断yamlfile文件是否存在； os.path.exists 文件存不存在
            self.yamlfile =yamlfile #存在赋值给 self.yamlfile
        else:
            raise FileNotFoundError("文件不存在") # 不存在就是提示

        #初始化中定义一个变量
        self._data = None
        self._data_all = None

    # 当个文档
    def data(self):
        #第一个调用data，读取yaml文档，如果_all不为空不是 ，直接返回之前保存的数据
        if not self._data:
            with open(self.yamlfile,"rb") as f:  #读取
                self._data = yaml.safe_load(f)
        return  self._data

    # 多个文档
    def data_all(self):
        #第一个调用data，读取yaml文档，如果_data_all不为空不是 ，直接返回之前保存的数据
        if not self._data_all:
            with open(self.yamlfile,"rb") as f:
                self._data_all = list(yaml.safe_load_all(f))
        return  self._data_all