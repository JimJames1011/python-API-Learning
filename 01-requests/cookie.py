#在headers参数中携带cookie
import requests
url = 'http://github.com/exle-morganna'

#构建请求头
headers={
    'User-Agent':Mozilla
    'Cookie':
}

response = requests.get(url,headers=headers)

with open("Drama_Intensity_Dataset.xlsx","wb") as f:
    f.write(response.content)
