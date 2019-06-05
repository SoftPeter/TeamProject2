# coding=utf-8
import os
import sys
import urllib.request
import json
#from collections import defaultcollect
from collections import defaultdict

client_id = "cK6hiCGUYGToHXvSKYrK"
client_secret = "jVQAvQKBXS"
encText = urllib.parse.quote("고등어")
url = "https://openapi.naver.com/v1/search/shop?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    result = json.loads(response_body.decode('utf-8'))
   # print(response_body.decode('utf-8'))
   # items = result.get('items')
   # print(result)
    items = result.get('items')

    payload = []
    for item in items:
        container = defaultdict()  # from collections import defaultcollect 불러와야
        props = ['title', 'link' 'image']
        for prop in props:
            container[prop] = item.get(prop, None)
        payload.append(container)
        print(payload)

else:
    print("Error Code:" + rescode)
