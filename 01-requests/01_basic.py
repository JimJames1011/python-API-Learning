#请求
#发送http请求 获得响应数据
import requests
ur1="http://www.baidu.com"
res=requests.get(ur1)
print(res.text)
