#发送带参数的请求
#url中直接带参数
import requests

url="https://www.baidu.com/s?wd=python"
headers={
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36 Edg/153.0.0.0}'}
response=requests.get(url,headers=headers)
with open("baidu.html","wb")as f:
    f.write(response.content)

#通过params携带参数字典
import requests
headers={
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36 Edg/153.0.0.0}'}
url="https://www.baidu.com/?"
kw={'wd':'python'}
response=requests.get(url,headers=headers,params=kw)
print(response.content)

#练习
params={'name':'Jim',
        'age':19}
response=requests.get(url,params=params)
print(response.content)
