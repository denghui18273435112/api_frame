#yaml_demo.py
import  yaml
from utils.YamlUtil import YamlReaber

#单个文件
res = YamlReaber("./data.yaml").data()
print(res)

#读取多个文件
tt = YamlReaber("./data.yaml").data_all()
print(tt)



#单个文档读取
# with open("./data.yaml","r",encoding='UTF-8') as f:  #打开文件
#     r= yaml.safe_load(f)                              # #使用yaml方法读取;参与方法safe_load() 读取单个文档；如果是多个文档则用safe_load_all()
#     print(r)

#读取多个文件
# with open("./data.yaml","r",encoding='UTF-8') as f:
#     r = yaml.safe_load_all(f)   #使用yaml方法读取;参与方法safe_load() 读取单个文档；如果是多个文档则用safe_load_all()
#     print(type(r))
#     for t in r:
#         print(t)
