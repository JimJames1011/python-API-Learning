#api
import os
api_key=os.getenv("API_KEY")
print(api_key)


#练习
import requests
import os

api_key=os.getenv("API_KEY")

headers={
    "Authorization": f"Bearer{api_key}"
}

data={

}

response=requests.post(
    json=data,
    headers=headers
)

result=response.json()
print(result)
