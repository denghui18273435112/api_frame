#yaml_demo.py
import yaml     # 导入yaml包
from utils.YamlUtil import YamlReaber    #导入二次封装的包

#分三步：
#第一步：创建一个yaml格式的文件；yaml格式的文件以yaml为后缀；
#第二步：读取这个文件
#第三步：输出这个文件内容


res = YamlReaber("./data-dan.yaml").data()    #读取单个文件； YamlReaber("./data-duo.yaml") 初始化需要读取的文件；调用.data() 方法输出
print(res)                                #打印输出

tt = YamlReaber("./data-duo.yaml").data_all()   #读取多个文件； YamlReaber("./data-duo.yaml") 初始化需要读取的文件；调用.data_all() 方法输出
print(tt)                                     #打印输出


with open("./data-dan.yaml","r",encoding='UTF-8') as f:  #打开文件；encoding='UTF-8'避免出现中文乱码
    r= yaml.safe_load(f)                                #使用yaml方法读取;方法safe_load() 读取单个文档；
    print(r)                                            #打印输出

with open("./data-duo.yaml","r",encoding='UTF-8') as f: #打开文件；encoding='UTF-8'避免出现中文乱码
    r = yaml.safe_load_all(f)                           #使用yaml方法读取;多个文档则用safe_load_all()
    for t in r:                                        #r返回的是对象，需要循环遍历
        print(t)                                        #打印输出
