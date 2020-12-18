
# coding:utf-8
import requests

host = 'http://192.168.1.66/zentao/api-getsessionid.json'

#url = host + '/zentao/user-login.html'


req = requests.get(url)

print(req.headers)



h1 = {
"Accept": "application/json, text/javascript, */*; q=0.01",
"X-Requested-With": "XMLHttpRequest",
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
"Referer": "http://192.168.1.66:8088/zentao/user-login.html",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,lb;q=0.7"
}


data = {
    'account': 'admin',
    'password': '123456',
    'referer': host+ '/zentao/',
    'keepLogin': 1
}

r = requests.post(url, data=data, headers=h1)

print(r.headers)