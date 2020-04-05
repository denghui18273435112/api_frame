# coding=utf-8
from config.Conf import ConfigYaml
from utils.MysqlUitl import Mysql
def init_db(db_alias):
    db_info = ConfigYaml().get_db_conf_info(db_alias)
    host  = db_info["db_host"]
    user  = db_info["db_user"]
    password  = db_info["db_password"]
    database  = db_info["db_database"]
    port  = int(db_info["db_port"])
    charse  = db_info["db_charset"]

    conn =  Mysql(host,user,password,database,port,charse)
    return  conn

if __name__ == '__main__':
    init_db("db_1")


