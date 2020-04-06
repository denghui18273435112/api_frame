# coding=utf-8

# 第1步：导包
import pymysql
from utils.logUtil import my_log

class Mysql:
    def __init__(self,host,user,password,database,port,charset="utf8"):
        self.log = my_log()
        self.conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset = charset,
            port = port
        )
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)    #获取执行sql的光标对象  cursor=pymysql.cursors.DictCursor  把输入结果更改为字典格式

    def fetchone(self,sql):
        '''
        单个查询
        :param sql:
        :return:
        '''
        self.cursor.execute(sql)        #执行sql语句
        return self.cursor.fetchone()   #返回查询出来的数据

    def fetchalll(self,sql):
        '''
        多个查询
        :param sql:
        :return:
        '''
        self.cursor.execute(sql)        #执行sql语句
        return self.cursor.fetchall()  #返回查询出来的数据

    def exec(self,sql):
        '''
        执行
        :return:
        '''
        try:
            if self.conn and self.cursor:
                self.cursor.execute(sql)
                self.conn.commit()
        except Exception as ex:
            self.conn.rollback()
            self.log.error("mysql 执行失败")
            self.log.error(ex)
            return False
        return True

    def __del__(self):
        #关闭光标对象
        if self.cursor is not None:
            self.cursor.close()
        #关闭连接对象
        if self.conn is not None:
            self.conn.close()

if __name__ == '__main__':
    mysql = Mysql("211.103.136.242",
                  "test",
                  "test123456",
                  "meiduo",
                  7090,
                  charset="utf8")
    res = mysql.fetchalll("select username,password from tb_users")
    print(res)



# #  没有封装前的代码
#
#
# #第一个导pymysql
# import pymysql
#
# #  第2步：链接数据库
# """
# host 数据库地址；
# user、password 数据库账号和密码；
# database 连接的数据库；
# charset 编码集； port 端口
# """
# conn = pymysql.connect(
#     host="211.103.136.242",
#     user="test",
#     password="test123456",
#     database="meiduo",
#     charset = "utf8",
#     port = 7090
# )
#
# # 第3步：获取执行sql的光标对象
# cuesor = conn.cursor()
#
# # 第4步： 执行sql的方法 execute
# sql = "select username,password from tb_users"
# cuesor.execute(sql)
# # fetchone() 单条信息;fetchall()全部信息；
# res = cuesor.fetchone()
#
# print(res)
#
# # 第5步：关闭关闭对象；关闭数据库连接对象
# cuesor.close()
# conn.close()