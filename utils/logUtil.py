#封装log工具类

import logging
from config import Conf
import datetime
from config.Conf import ConfigYaml
import os

#定义日志级别的映射
log_l={
    "info":logging.INFO,
    "debug":logging.DEBUG,
    "warning":logging.WARNING,
    "error":logging.ERROR
}

class Logger:   #1 创建类
    #   #2定义参数；想想需要有哪些參數；生成日志文件名称、Logger名称、日志级别
    def __init__(self,log_file,log_Logger_name,log_level):
        self.log_file = log_file                    #扩展名；在配置文件写
        self.log_Logger_name = log_Logger_name      #Logger名称，不在配置文件写
        self.log_level = log_level                    #日志级别；在配置文件写

        self.logger_name = logging.getLogger(self.log_Logger_name)   #第一步：设置logger名称
        self.logger_name.setLevel(log_l[self.log_level])              #第二步：设置log级别

        if not self.logger_name.handlers:                            #判断handler是否存在
            #两种类型第一种：输出控制台·
            fh_stream = logging.StreamHandler()                 #第三步：创建handler
            fh_stream.setLevel(log_l[self.log_level])           #第四步：设置日志级别
            formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
            fh_stream.setFormatter(formatter)                   #第五步：定义格式

           #两种类型第二种：写入文件
            fh_file = logging.FileHandler(self.log_file,encoding='utf-8')            #第三步：写入文件的handler
            fh_file.setLevel(log_l[self.log_level])                  #第四步：设置日志级别
            #formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
            fh_file.setFormatter(formatter)                          #第五步：定义格式

            #第六步：添加handler
            self.logger_name.addHandler(fh_stream)
            self.logger_name.addHandler(fh_file)

#1、初始化参数数据
#日志文件名称、日志文件级别
#日志文件名称=log目录+当前时间+扩展名

log_path = Conf.get_log_path()  #log目录
current_time = datetime.datetime.now().strftime("%Y-%m-%d")  #当前时间
log_extensiong = ConfigYaml().get_conf_log_extensiong() #扩展名
logfile = os.path.join(log_path,current_time+log_extensiong)   #合并
#print(logfile)
loglevel = ConfigYaml().get_conf_log()  #日志文件级别
#print(loglevel)

#2、对方方法，初始log工具类，提供其它类使用
def my_log(log_Logger_name = __file__):
    return Logger(log_file=logfile,log_Logger_name=log_Logger_name,log_level=loglevel).logger_name

if __name__ == '__main__':
    my_log().debug("this debug isSS")





