# 导入logging的包
import  logging

#设置配置信息
logging.basicConfig(level=logging.INFO,format="%(asctime)s-%(name)s-%(levelname)s-%(message)s")

#定义日志的名称getlogger
logger = logging.getLogger("log_demo")

#输出
#INFO 级别是不输出debug的
logger.info("info")
logger.debug("debug")
logger.warning("warning")