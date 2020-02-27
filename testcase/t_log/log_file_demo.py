import logging
#输出控制条

#1设置logger名称
logger = logging.getLogger("log_file_demo")

#2设置log级别
logger.setLevel(logging.INFO)

#3创建heabler
fh_stream = logging.StreamHandler()
fh_file = logging.FileHandler("./test.log")

#4设置日志级别
#fh_stream.setLevel(logging.INFO)
fh_file.setLevel(logging.INFO)

#5定义输出格式
formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
#fh_stream.setFormatter(formatter)
fh_file.setFormatter(formatter)

#6添加handler
#logger.addHandler(fh_stream)
logger.addHandler(fh_file)

#7运行输出到控制台
logger.info("this is a info")
logger.info("this is a info-11")
logger.debug("this is a debug" )

