import  requests
from utils.RequestsUtil import *
from utils.RequestsUtil import Request
from config.Conf import ConfigYaml

"""
login_4	登录  登录成功
http://211.103.136.242:8064/authorizations/
POST	json
{"username":"python","password":"12345678"}
"""
def login():

	#http://211.103.136.242:8064
	url = ConfigYaml().get_conf_url()+"/authorizations/"
	data = {"username":"python","password":"12345678"}

	#原始
	# r= requests.post(url=url,data=data)
	# print(r.json())
	#第一次封装
	#return requests_post(url=url,data=data)
	#第一次重构
	return Request().post(url=url,data=data)


"""
info_2	个人信息	获取个人信息正确
http://211.103.136.242:8064/user/		GET	json
"""
def info():
	#url = "http://211.103.136.242:8064/user/"

	url = ConfigYaml().get_conf_url()+"/user/"
	token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Ijk1MjY3MzYzOEBxcS5jb20iLCJleHAiOjE1ODIwNzQwNTUsInVzZXJuYW1lIjoicHl0aG9uIiwidXNlcl9pZCI6MX0.oO3p5apP3SkfynUUEm9PSn3JGXXv9aNdP0ql5nuNY-w"
	headers = {"Authorization":"JWT "+token}

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
	url = ConfigYaml().get_conf_url()+"/categories/115/skus/"
	#url = "http://211.103.136.242:8064/categories/115/skus/"
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
	url = ConfigYaml().get_conf_url()+"/cart/"
	#url = "http://211.103.136.242:8064/cart/"
	data = {"sku_id":"3","count":"1","selected":"true"}
	token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Ijk1MjY3MzYzOEBxcS5jb20iLCJleHAiOjE1ODUyMDUzMTIsInVzZXJuYW1lIjoicHl0aG9uIiwidXNlcl9pZCI6MX0.jyxFvYviFaa57s9lP_23PPNw9h5iPGnT7a0I9XC_fGY"
	headers = {"Authorization":"JWT "+token}

	#原始
	# r= requests.post(url=url,data=data,headers=headers)
	# print(r.json())
	#第一次封装
	#return requests_post(url=url,data=data,headers=headers)

	#第一次重构
	return Request().get(url=url,data=data,headers=headers)


"""order_1	订单	保存订单	http://211.103.136.242:8064/orders/	登录	GET	json	{"address":"1","pay_method":"1"}
"""
def order():
	url = ConfigYaml().get_conf_url()+"/orders/"
	#url = "http://211.103.136.242:8064/orders/"
	data = {"address":"1","pay_method":"1"}
	token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Ijk1MjY3MzYzOEBxcS5jb20iLCJleHAiOjE1Nzk0MzE4NTcsInVzZXJuYW1lIjoicHl0aG9uIiwidXNlcl9pZCI6MX0.Y2DDZSwgJt6ykmfFhKr71EpL8glDGrx_gtFeSqdGH-o"
	headers = {"Authorization":"JWT "+token}

	#原始
	# r= requests.post(url=url,data=data,headers=headers)
	# print(r.json())
	#第一次封装
	#return requests_post(url=url,data=data,headers=headers)
	#第一次重构
	return Request().post(url=url,data=data,headers=headers)


if __name__ == '__main__':

    #print(login())

	#print(info())
    #print(goods_list())
    print(cart())
    #print(order())

