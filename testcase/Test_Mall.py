import  requests
from utils.RequestsUtil import *
from utils.RequestsUtil import Request
from config.Conf import ConfigYaml
from common.Base import init_db

"""
login_4	登录  登录成功	http://211.103.136.242:8064/authorizations/
POST	json			{"username":"python","password":"12345678"}
"""
def login1():
	url = ConfigYaml().get_conf_url()+"/authorizations/"	# 调用封装方法，获取url地址
	data = {"username":"python","password":"12345678"}

	# r= requests.post(url=url,data=data)		#原始
	# print(r.json())

	#return requests_post(url=url,data=data)	#第一次封装

	r = Request().post(url=url,data=data)	#第一次重构
	body = r["body"]
	print(body)

	conn = init_db("db_1")
	res_db = conn.fetchone("select id,username from tb_users where username='python' ")
	print("数据库查询结果",res_db)

	user_id = body["user_id"]

	#assert user_id == res_db["id"]
	
	if user_id == res_db["id"]:
		print("验证成功")
	else:
		print("验证失败")


def login():
	url = ConfigYaml().get_conf_url()+"/authorizations/"	# 调用封装方法，获取url地址
	data = {"username":"python","password":"12345678"}

	# r= requests.post(url=url,data=data)		#原始
	# print(r.json())

	#return requests_post(url=url,data=data)	#第一次封装

	return Request().post(url=url,data=data)	#第一次重构

"""
info_2	个人信息	获取个人信息正确
http://211.103.136.242:8064/user/		GET	json
"""
def info():
	token_new = login()["boby"]["token"]			# 调用登陆成功后返回的token
	url = ConfigYaml().get_conf_url()+"/user/"		# 调用封装方法，获取url地址
	headers = {"Authorization":"JWT "+token_new}

	#原始
	# r= requests.get(url=url,headers=headers)
	# print(r.json())

	#第一次封装
	#return requests_get(url=url,headers=headers)

	#第一次重构
	return Request().get(url=url,headers=headers)

"""
商品列表数据	商品列表数据正确	http://211.103.136.242:8064/categories/115/skus/
GET	json	{""page:"1","page_size":"10","ordering":"create_time"}
"""
def goods_list():
	url = ConfigYaml().get_conf_url()+"/categories/115/skus/"		#ConfigYaml().get_conf_url() 获取yaml文件中的url
	data = {"page":"1","page_size":"10","ordering":"create_time"}

	#原始
	# r= requests.get(url=url,data=data)
	# print(r.json())

	#第一次封装
	#return requests_get(url=url,data=data)

	#第一次重构
	return Request().get(url=url,data=data)

"""cart_1	购物车	添加购物车成功	http://211.103.136.242:8064/cart/
登录	GET	json	{"sku_id":"3","count":"1","selected":"true"}
"""
def cart():
	token_new = login()["boby"]["token"]		# 调用登陆成功后返回的token
	url = ConfigYaml().get_conf_url()+"/cart/"
	data = {"sku_id":"3","count":"1","selected":"true"}
	headers = {"Authorization":"JWT "+token_new}

	#原始
	# r= requests.post(url=url,data=data,headers=headers)
	# print(r.json())

	#第一次封装
	#return requests_post(url=url,data=data,headers=headers)

	#第一次重构
	return Request().get(url=url,data=data,headers=headers)

"""order_1	订单	保存订单	http://211.103.136.242:8064/orders/	登录	GET	json	{"address":"1","pay_method":"1"}
"""
def order():										#方法存在问题
	token_new = login()["boby"]["token"]			#调用登陆成功后返回的token
	url = ConfigYaml().get_conf_url()+"/orders/"	# 调用封装方法，获取url地址
	data = {"address":"1","pay_method":"1"}
	headers = {"Authorization":"JWT "+token_new}

	#原始
	# r= requests.post(url=url,data=data,headers=headers)
	# print(r.json())

	#第一次封装
	#return requests_get(url=url,data=data,headers=headers)

	#第一次重构
	return Request().post(url=url,data=data,headers=headers)

if __name__ == '__main__':
	#goods_list()
	#print(info())
	#print(goods_list())

    #print(order())
	#pprint(cart(),indent=2)
	print(login1())
