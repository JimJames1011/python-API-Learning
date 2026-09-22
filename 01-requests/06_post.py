#post
import requests
url='http://www.baidu.com'
data={
    'username':'Jim',
    'password':123456
}
response=requests.post(url,data=data)
