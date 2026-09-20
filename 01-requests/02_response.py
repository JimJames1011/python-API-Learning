#responde响应对象
import requests
ur1="http://www.baidu.com"
res=requests.get(ur1)
#print(res.text)
#res.text 类型：str  自行推测的文字编码
print(res.content.decode())
#res。content 类型：bytes

#responde 常见的响应对象参数和方法
#相应url
import requests
ur1="http://www.baidu.com"
res=requests.get(ur1)

#状态码
print(res.status_code)

#相应对应的请求头
print(res.request.headers)
#响应头
print(res.headers)

#打印响应设置cookies
print(res.cookies)
