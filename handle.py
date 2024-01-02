# -*- coding: utf-8 -*-
# filename: handle.py

import hashlib
import web
import reply
import receive
import json
import requests
import pathlib
import textwrap
import threading
import time
import xml.etree.ElementTree as ET
from reply import TextMsg

response_cache = {}


def clear_cache():
    global response_cache
    # Clear cache
    response_cache = {}
    print("Cache cleared at", time.ctime())

    # Restart timer
    threading.Timer(500, clear_cache).start()


def start_clear_cache_timer():
    # Clear cache per 60s
    threading.Timer(500, clear_cache).start()

class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "" #Depends on your WeChat config

            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            # Updated to be compatible with Python 3
            sha1.update(list[0].encode('utf-8'))
            sha1.update(list[1].encode('utf-8'))
            sha1.update(list[2].encode('utf-8'))
            hashcode = sha1.hexdigest()
            print("handle/GET func: hashcode, signature: ", hashcode, signature)
            print("TestINFO", echostr);
            if hashcode == signature:
                print("TEST INFO: hashcode match signature")
                return echostr
            else:
                print("TEST INFO: hashcode does not match signature")
                return ""
        except Exception as Argument:  # Updated to be compatible with Python 3
            return Argument

    def POST(self):
        try:
            webData = web.data()
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                content = recMsg.Content

                print("\nToUser=", toUser + "\n")

                #To hash
                request_hash = hashlib.md5(content).hexdigest()
                if request_hash in response_cache:
                    cache_content = response_cache[request_hash]
                    replyMsg = TextMsg(toUser, fromUser, cache_content)
                else:
                    # Send request to Gemini apis
                    response = self.get_gemini_response(content)
                    replyMsg = TextMsg(toUser, fromUser, response)
                    response_cache[request_hash] = response

                return replyMsg.send()
            else:
                return "success"
        except Exception as e:
            print(e)
            return "Error"

    def get_gemini_response(self, text):
        headers = {'Content-Type': 'application/json'}
        textUTF8 = text.decode('utf-8')
        data = {
            "contents": [
                {
                    "role": "user",
                    "parts": [{"text": textUTF8}]
                }
            ]
        }
        print("data = ", data)
        apiKey = ""  # Gemini API key field
        response = requests.post(
            "https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key=" + apiKey,
            headers=headers,
            data=json.dumps(data)
        )
        # 解析响应
        response_json = response.json()
        gemini_text = response_json['candidates'][0]['content']['parts'][0]['text']
        return gemini_text

start_clear_cache_timer()

