#json
import requests
url="http://httpbin.org/get"
response=requests.get(url)
print(response.status_code)
data=response.json()
print(data)
print(data['url'])
print(data['headers'])


#json+post
import requests
url="http://httpbin.org/post"
data={
    'name':'Jim',
    'age':20
}
response=requests.post(url,data=data)
result=response.json()
print(result)
