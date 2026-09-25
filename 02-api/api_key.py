import os
import requests

url="http://api.deepseek.com/chat/completions"

api_key=os.getenv("API_KEY")

headers={
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data={
    "model":"deepseek-flash",
    "message":[{
        "role":"user",
        "content":"请用一句话介绍python"
    }]
}

response=requests.post(url,json=data,headers=headers)

print(response.status_code)
