
import requests
import json
import os

import hashlib
import web
import pathlib
import textwrap
import threading
import time
import xml.etree.ElementTree as ET

# 替换为Gemini API Key
API_KEY = ""

def get_gemini_response(text):

    # 设置请求头和请求体
    headers = {'Content-Type': 'application/json'}
    data = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": text}]
            }
        ]
    }
    print("data = ", data)
    apiKey = ""  # 替换为Gemini API Key
    response = requests.post(
        "https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key=" + apiKey,
        headers=headers,
        data=json.dumps(data)
    )

    # 解析响应
    response_json = response.json()
    gemini_text = response_json['candidates'][0]['content']['parts'][0]['text']
    print("\n通过Gemini获取响应内容\n")
    return gemini_text


import gradio as gr

with gr.Blocks() as demo:  # 构建界面

    prompt = gr.Textbox(label="输入框")  # 文本输入框
    output = gr.Textbox(label="输出框")  # 文本输出框

    greet_btn = gr.Button("聊天")  # 按钮控件

    greet_btn.click(fn=get_gemini_response, inputs=prompt, outputs=output)

demo.launch(share=True)
