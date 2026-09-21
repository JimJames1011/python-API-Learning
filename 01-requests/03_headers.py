import requests
import urllib3

response=requests.get("http://baidu.com")
print(response.content)
url="http://baidu.com"

#requests发送请求
#发送带header的请求
response=requests.get("http://www.baidu.com")
print(response.content.decode())
print(response.request.headers)
print(len(response.content.decode()))

#构建请求头字典
headers={
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36 Edg/153.0.0.0}'}
#发送带请求头的请求
response1=requests.get(url,headers=headers)
print(response1.content)
print(len(response1.content.decode()))
