import requests
from utils.logUtil import my_log
from pprint import pprint
from config.Conf import ConfigYaml

#重构requests库中的post方法、get方法  使用中
class Request:

	def __init__(self):
		self.log = my_log("自定义封装")

	def request_api(self,url,headers=None,data=None,json=None,cookies=None,method="get"):
		"""
		:param url: 必传
		:param headers: 默认不传
		:param data: 默认不传
		:param json: 默认不传
		:param cookies: 默认不传
		:param method: 默认为get
		:return:  res字典由code和body组成
		#status_code获取状态码
		"""
		if method=="get":
			self.log.debug("发送get请求")
			r = requests.get(url=url,headers=headers,data=data,cookies=cookies)
		elif method=="post":
			self.log.debug("发送post请求")
			r = requests.post(url=url,headers=headers,data=data,json=json,cookies=cookies)
		try:
			body = r.json()
		except Exception as e:
			body = r.text
		res =dict()
		res["code"] = r.status_code
		res["body"] = body
		return res

	def get(self,url,**kwargs):
		"""
		:param url:  接口地址
		:param kwargs: 不定参数: *args和**kwargs 可以接受任意长度和格式的参数；两个参数不能同时传，一次只能传一个
		:return: 调用request_api方法,method默认为get,并且传入随意参数;request_api方法支持headers,data,json,cookies
		"""
		return self.request_api(url,method="get",**kwargs)

	def post(self,url,**kwargs):
		"""
		:param url:  接口地址
		:param kwargs: 不定参数: *args和**kwargs 可以接受任意长度和格式的参数；两个参数不能同时传，一次只能传一个
		:return: 调用request_api方法,method默认为post,并且传入随意参数;request_api方法支持headers,data,json,cookies
		"""
		return self.request_api(url,method="post",**kwargs)

if __name__ == '__main__':
	# url = ConfigYaml().get_conf_url()+"/authorizations/"
	# data = {"username":"python","password":"12345678"}
	# print(Request().post(url=url,data=data))
	url ="http://192.168.1.66:8088/zentao/api-getsessionid.json"
	headers ={"Host":"<calculated when request is sent>",
			  "User-Agent":"PostmanRuntime/7.26.8",
			  "Accept":"*/*",
			  "Accept-Encoding":"gzip, deflate, br",
			  "Connection":"keep-alive",
			  "Cookie":"lang=zh-cn; device=desktop; theme=default; lastProject=1; lastProduct=1; lastTaskModule=0; preProductID=1; preBranch=0; bugModule=0; bugBranch=0; treeBranch=0; qaBugOrder=id_desc; zentaosid=7o6sngqg9mp01dmhmg38m3d6i1",
			  "Postman-Token":"<calculated when request is sent>"}
	print(requests.get(url=url,headers=headers))


