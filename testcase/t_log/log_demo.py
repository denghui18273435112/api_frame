import  logging # 1导入logging的包

logging.basicConfig(level=logging.INFO,format="%(asctime)s-%(name)s-%(levelname)s-%(message)s") #2设置配置信息;level 级别；format 格式
logger = logging.getLogger("log_demo")  #3定义日志的名称getlogger

#4输出    INFO 级别是不输出debug的
logger.info("info")
logger.debug("debug")
logger.warning("warning")