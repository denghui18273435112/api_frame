# coding=utf-8
import  re
f=open("ss.log","rb",) #打开日志文件
for i in f:  #逐行遍历文件
    #text=re.findall('12422222222 签名: sign=【趣生财钱包】 内容：验证码(\d+)',i) #获取指定号码的验证码
    print(i)
