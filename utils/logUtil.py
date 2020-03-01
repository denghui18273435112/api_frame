#封装log工具类
#1 创建类
import logging
from config import Conf
import datetime
from config.Conf import ConfigYaml
import os

#定义日志级别的隐射
log_l={
    "info":logging.INFO,
    "debug":logging.DEBUG,
    "warning":logging.WARNING,
    "error":logging.ERROR
}
class Logger:
#2定义参数
    #输出日志文件名称、Logger名称、日志级别
    def __init__(self,log_file,log_name,log_evel):
        self.log_file = log_file  #扩展名固定；配置文件
        self.log_name = log_name    #参数 不放配置文件
        self.log_evel = log_evel    #配置文件

        self.logger = logging.getLogger(self.log_name)   #1设置logger名称
        self.logger.setLevel(log_l[self.log_evel])      #2设置log级别
        if not self.logger.handlers:                    #判断handler是否存在
            #两种类型第一种：输出控制台·
            # fh_stream = logging.StreamHandler()
            # fh_stream.setLevel(log_l[self.log_evel])
            # formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
            # fh_stream.setFormatter(formatter)
            # self.logger.addHandler(fh_stream)



           #两种类型第二种：写入文件
            fh_file = logging.FileHandler(self.log_name)
            fh_file.setLevel(log_l[self.log_evel])
            formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
            fh_file.setFormatter(formatter)
            #添加handler
            self.logger.addHandler(fh_file)

#1、初始化参数数据
#日志文件名称、日志文件级别
#日志文件名称=log目录+当前时间+扩展名

log_path = Conf.get_log_path()  #log目录
current_time =datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")  #当前时间
log_extensiong = ConfigYaml().get_conf_log_extensiong() #扩展名
logfile = os.path.join(log_path,current_time+log_extensiong)    #合并
print(logfile)

loglevel = ConfigYaml().get_conf_log()  #日志文件级别
#print(loglevel)

#2、对方方法，初始log工具类，提供其它类使用
def my_log(log_name=__file__):
    return Logger(log_file=logfile,log_name=log_name,log_evel=loglevel).logger


if __name__ == '__main__':
    my_log().debug("dad")






