import requests

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
	def request_api(self,url,headers=None,data=None,json=None,cookies=None,method="get"):
		if method=="get":
			r = requests.get(url=url,headers=headers,data=data,cookies=cookies)
		elif method=="post":
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
