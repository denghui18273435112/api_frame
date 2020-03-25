import requests
from utils.logUtil import my_log
from pprint import pprint
#自定义方法;requests库中的get方法
def requests_get(url,headers=None,data=None):
	r = requests.get(url=url,headers=headers,data=data)
	code = r.status_code
	try:
		boby = r.json()
	except Exception as e:
		boby = r.text
	res =dict()
	res["code"] = code
	res["boby"] = boby
	return res

#自定义方法;requests库中的post方法
def requests_post(url,headers=None,data=None,json=None):
	r = requests.post(url=url,headers=headers,data=data,json=json)
	code = r.status_code
	try:
		boby = r.json()
	except Exception as e:
		boby = r.text
	res =dict()
	res["code"] = code
	res["boby"] = boby
	return res

#重构requests库中的post方法、get方法
class Request:

	def __init__(self):
		self.log = my_log("自定义封装")

	def request_api(self,url,headers=None,data=None,json=None,cookies=None,method="get"):
		if method=="get":
			self.log.debug("发送get请求")
			r = requests.get(url=url,headers=headers,data=data,cookies=cookies)
			code = r.status_code

		elif method=="post":
			self.log.debug("发送post请求")
			r = requests.post(url=url,headers=headers,data=data,json=json,cookies=cookies)
			code = r.status_code

		try:
			boby = r.json()
		except Exception as e:
			boby = r.text
		res =dict()
		res["code"] = code
		res["boby"] = boby
		return res

	def get(self,url,**kwargs):
		return self.request_api(url,method="get",**kwargs)

	def post(self,url,**kwargs):
		return self.request_api(url,method="post",**kwargs)
