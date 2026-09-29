import os

import app
import requests
from fastapi import FastAPI
from pydantic import BaseModel

spp=FastAPI()

#用户请求的数据结构
class ChatRequest(BaseModel):
    message:str

#调用deepseek API
def ask_ai(prompt:str):
    api_key=os.getenv("API_KEY")

    url="http://api.deepseek.com/chat/completions"

    headers={
        "Authorization":f"Beaer {api_key}",
        "content-type":"application/json"
    }

    data={
        "model":"deepseek-flash",
        "message":{
            "role":"user",
            "content":prompt
        }
    }

    response=requests.post(url,headers=headers,json=data)
    result=response.json()
    return result

#测试Fastapi
@app.get("/")
def home():
    return {
        "message":"FastAPI is running"
    }

#GET 参数
@app.get("/hello")
def hello(name:str):
    return{"message":f"Hello {name}!"}

#JSON+POST+Pydantic
@app.post("/chat")
def chat(request:ChatRequest):
    answer=ask_ai(request.message)

    return{
        "question":request.message,
        "answer":answer
    }
