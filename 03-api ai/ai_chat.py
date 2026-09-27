import os
import requests

def answer(prompt):
    api_key=os.getenv("API_KEY")
    
    url="http://api.deepseek.com/chat/completions"
    
    headers={
        "Authorization":f"Bearer{api_key}",
        "Content-type":"aplication/json"
    }
    data={
        "model":"deepseek-flash",
        "text":[{
            "role":"user",
            "content":prompt
        }]
    }
    
    response=requests.post(url,headers=headers,json=data)
    
    result=response.json()
    return result
    
while True:
    prompt=input("Please enter your prompt:")
    if prompt=="exit":
        break
    answer(prompt)
    print("AI:",answer)
