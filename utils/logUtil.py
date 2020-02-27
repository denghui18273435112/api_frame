#log工具类
#1 创建类
import logging



#定义日志级别的隐射
log_l={
    "info":logging.INFO,
    "debug":logging.DEBUG,
    "warning":logging.WARNING,
    "error":logging.ERROR
}
class Logger:
#2定义参数
    #输出文件名称、Loggername、日志登录
    def __init__(self,log_file,log_name,log_evel):
        self.log_file = log_file
        self.log_name = log_name
        self.log_evel = log_evel
        #1设置logger名称
        self.logger = logging.getLogger(self.log_file)

        #2设置log级别
        self.logger.setLevel(log_l[self.log_evel])

        #判断handler是否存在
        if not self.logger.handlers:

            #3输出控制台·
            fh_stream = logging.StreamHandler()
            fh_stream.setLevel(log_l[self.log_evel])
            formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
            fh_stream.setFormatter(formatter)

            #3写入文件
            fh_file = logging.FileHandler(self.log_file)
            fh_file.setLevel(log_l[self.log_evel])
            #formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
            fh_file.setFormatter(formatter)

            #添加handler
            self.logger.addHandler(fh_stream)
            self.logger.addHandler(fh_file)
#3 输出控制台