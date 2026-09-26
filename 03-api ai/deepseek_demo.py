import os
import requests

def ask_ai(prompt):
    api_key=os.getenv("API_KEY")

    url="http://api.deepseek.com/chat/completions"

    headers={
        "Authorization":f"Bearer{api_key}",
        "Content_type":"application/json"
    }

    data={
        "model":"deepseek-flash",
        "message":[{
            "role":"user",
            "content":prompt
        }]
    }

    response=requests.post(url,headers=headers,json=data)

    result=response.json()

    answer=result["message"]["content"]

    return answer

answer=ask_ai("What is python")
print(answer)
