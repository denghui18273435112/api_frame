import logging

#输出控制台
# logger = logging.getLogger("log_file_demo")#1设置logger名称
# logger.setLevel(logging.INFO)               #2设置log级别
# fh_stream = logging.StreamHandler()         #3创建heabler
# fh_stream.setLevel(logging.INFO)            #4设置日志级别
# formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
# fh_stream.setFormatter(formatter)           #5定义输出格式
# logger.addHandler(fh_stream)                #6添加handler
# logger.info("this is a info")             #7运行输出到控制台
# logger.info("this is a info-11")
# logger.debug("this is a debug" )          #log级别INFO时，不打印debug类型数据；原因info级别小于debug级别，所以不打印

#输出到日志文件中
logger = logging.getLogger("log_file_demo")     #1设置logger名称
logger.setLevel(logging.INFO)                     #2设置log级别
fh_file = logging.FileHandler("./test.log")     #3创建heabler
fh_file.setLevel(logging.INFO)                   #4设置日志级别
formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
fh_file.setFormatter(formatter)                 #5定义输出格式
logger.addHandler(fh_file)                      #6添加handler
logger.info("this is a info")                 #7运行打印到日志文件中
logger.info("this is a info-11")
logger.debug("this is a debug" )              #log级别INFO时，不打印debug类型数据；原因info级别小于debug级别，所以不打印

