#  没有封装前的代码


#第一个导pymysql
import pymysql

#  第2步：链接数据库
"""
host 数据库地址；
user、password 数据库账号和密码；
database 连接的数据库；
charset 编码集； port 端口
"""
conn = pymysql.connect(
    host="211.103.136.242",
    user="test",
    password="test123456",
    database="meiduo",
    charset = "utf8",
    port = 7090
)

# 第3步：获取执行sql的光标对象
cuesor = conn.cursor()

# 第4步： 执行sql的方法 execute
sql = "select username,password from tb_users"
cuesor.execute(sql)
# fetchone() 单条信息;fetchall()全部信息；
res = cuesor.fetchone()

print(res)

# 第5步：关闭关闭对象；关闭数据库连接对象
cuesor.close()
conn.close()