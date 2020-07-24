import re

def yzm(mobilnum):
    with open("test.log","r") as name:
            for line in name:
                yzm1=re.findall(str(mobilnum) +r' 签名: sign=【趣生财钱包】 内容：验证码(\d+)',line)
                print(yzm1)

if __name__=="__main__":
    logpath=""
    mobilnum=12422222223
    yzm(mobilnum)




