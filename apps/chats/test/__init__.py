#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2023/2/11 12:52
# @Author  : gy
# @File    : __init__.py.py
# @Software: PyCharm
import requests
import json

url = "http://127.0.0.1:8000/chat/"

payload = json.dumps({
   "content": "hahah"
})
headers = {
   'X-CSRFToken': 'O6QU8r9Sycp2RwLkZcpYwbCG9V6atcSd7TjpwCOnlAa0lXN3BReBEzXGgzFJmn9v',
   'Accept': 'application/json',
   'Content-Type': 'application/json',
   'Host': '127.0.0.1',
   'Connection': 'keep-alive'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
