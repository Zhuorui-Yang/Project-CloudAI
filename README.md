# Project-CloudAI
This is an open-source project for those users who want to build their own private AI assistant cross by WeChat and Cloud Servers.
Project CloudAI是一个开源的轻量级AI助手部署工具，目的是让没有编程经验的普通用户也能轻易部署属于自己的私服AI助手。

![CoverPic]([https://private-user-images.githubusercontent.com/82684293/293686261-289f75d0-c0f0-4339-b3a5-d4e14958a5a8.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDQxOTcyNjQsIm5iZiI6MTcwNDE5Njk2NCwicGF0aCI6Ii84MjY4NDI5My8yOTM2ODYyNjEtMjg5Zjc1ZDAtYzBmMC00MzM5LWIzYTUtZDRlMTQ5NThhNWE4LmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAxMDIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMTAyVDEyMDI0NFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTUxOGJiM2IxOTRkYjM1NGZjMjUwZGNkYmUzYTA3ZDcxOGVmZjUzMjg5YjE1MTQ4MzJiM2IxOTAwZDYzMmRiZTEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.6Qi4saHP-lTSU3BL_ZPEItBzGrrr4wlDW2v7sRlItHI](https://private-user-images.githubusercontent.com/82684293/293686261-289f75d0-c0f0-4339-b3a5-d4e14958a5a8.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MTg1MjIyNjIsIm5iZiI6MTcxODUyMTk2MiwicGF0aCI6Ii84MjY4NDI5My8yOTM2ODYyNjEtMjg5Zjc1ZDAtYzBmMC00MzM5LWIzYTUtZDRlMTQ5NThhNWE4LmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA2MTYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNjE2VDA3MTI0MlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWUzYzVhY2MyMTIyYTg0NzVkMTU5ZDg0NTVhZTIyNTE4NDE5ZDJlMTUzMmYyODE2YjQxYzNmNzM3OGQ5ZDFmNmImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.T5pzDj-wNJmHdbps7ZRt9XFVe4GmMkLcjx7wJFjuwPg))

/**

本文档是开源项目Project CloudAI的开发文档，本项目主要是为没有编程经验的普通用户提供一个私服云端AI的简易部署方式。本项目提供两种部署方式：云端请求服务提供商接口和云端本地化部署。

当前版本（V1.0）仅支持请求Google Gemini的google-apis接口，后续版本计划接入OpenAI ChatGPT和百度文言一心。

本文档对应的版本号为V1.0（01/12/2024）。

本文档及项目源码已隐去API Key、Token等敏感信息，相关字段的赋值逻辑需要开发者自行配置。

项目地址：[https://github.com/Zhuorui-Yang/Project-CloudAI/](https://github.com/Zhuorui-Yang/Project-CloudAI/tree/main)

*/

- **1  事前环境配置**
    
    部署本项目所需要的前置环境如下：
    
    - 一台可以请求google-apis的云服务器
    - Python3环境（或Python2.7以上，但需要对源码进行向下兼容）
    - web.py
    - libxml2
    - libxslt
    - lxml python
    - 对应服务供应商的API Key
    - 一个微信公众号（无需微信认证，有基础的接收消息和被动回复功能即可）
      
- **2  项目结构**
- 
    - **2.1 项目源码结构**
        
        项目根目录默认包含本项目的所有.py文件。如果开发者只需要使用其中的特定功能，则可以适当解耦和删减根目录文件。例如，如果只需要使用Gemini的文字问答功能，只需要将main.py、handle.py、receive.py和reply.py文件部署到云服务器的同一路径下，然后删减源码中的无效引用即可。此处介绍四个重要的.py文件：
        
        - main.py：项目启动器，定义了/wx路径，接收传参并挂起服务。
        - handle.py：负责处理接收到的GET/POST请求，缓存已生成的响应内容，根据历史调用状况选择直接返回缓存内容或请求服务供应商的接口。另外，它包含了一个清除缓存的定时器，默认的缓存清除间隔是500s，开发者可以根据自己的服务器状况进行适当调整。
        - receive.py：处理来自微信服务器的请求消息，预置文本消息和图片消息处理。
        - [reply](http://reply.py).py:  根据传参生成对微信服务器的请求报文并发送，预置文本消息处理。
        
        注意，以上文件均是基于Python3所写成的，如果开发者使用的是Python2.7或以上的环境，可能需要对源码进行兼容性修改。

        //项目结构图待补全，有空再做
        
    - **2.2 微信服务器验证逻辑**
        
        当开发者配置微信公众号的时候，微信服务端的实际逻辑如下：
 
      ![WeChatAuth](https://private-user-images.githubusercontent.com/82684293/293689301-c145df19-04f5-482f-a01e-4ac76d8e518f.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDQxOTc4MTAsIm5iZiI6MTcwNDE5NzUxMCwicGF0aCI6Ii84MjY4NDI5My8yOTM2ODkzMDEtYzE0NWRmMTktMDRmNS00ODJmLWEwMWUtNGFjNzZkOGU1MThmLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAxMDIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMTAyVDEyMTE1MFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWEyYWJiYzVjNTM1MmYwZTEzZDQ2MWVkNmU2YTBjODExNjdjNzE5ZDViOTVmYmQ0N2QzYTkxNzNlNzhiYTJkZjYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.9lu3l4Ooz5Zr1uggpFsbXLYwH31WWORv7W8sQACyqsQ)
        
    - **2.3 接收公众号消息/被动回复公众号消息逻辑**
        
        建议参考官方文档: https://developers.weixin.qq.com/doc/offiaccount/Message_Management/Receiving_standard_messages.html

        ![WeChatResponse](https://private-user-images.githubusercontent.com/82684293/293689304-e637ebe5-6e9a-4dee-bae6-1497026bba0e.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDQxOTc4MTAsIm5iZiI6MTcwNDE5NzUxMCwicGF0aCI6Ii84MjY4NDI5My8yOTM2ODkzMDQtZTYzN2ViZTUtNmU5YS00ZGVlLWJhZTYtMTQ5NzAyNmJiYTBlLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDAxMDIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwMTAyVDEyMTE1MFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTQzZTEwZWUyZDVmN2UzZGM5ZmJmMGRkYzk4MWExYmI5YmJkN2MwMjNiYjFkMWIyYjIxYmU5MGU0OTM4MDEwOTUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.35d3PlXli8R9-olyTTrgR8ERPUsdAH5tP2mdKiw3obw)
        
    - **3  云服务器端配置**
    
        本项目的代码结构非常简单，只需要将指定功能所需要的文件添加到同一指定路径下，并通过下述命令启动:

        python main.py 80
        
        启动后将会挂起一个监听80端口的进程，用于接收来自微信服务器的消息。注意：由于微信API开发规范，端口号只能且必须是80。
      
    - **4  微信公众号配置**
     
          有空再写
    - **5  重要代码解释**

          有空再写
    - **6  修改与调试建议**

          有空再写
    - **7  已知缺陷/安全风险**
    - 
          - 由于微信API开发规范限制，main.py只能监听80端口。众所周知，这是一个高风险的行为，因此我们建议开发者通过端口映射等方式规避该风险，或者不要在服务器上挂载任何可能导致敏感信息泄露的进程。如果开发者选择非微信的客制化第三方平台，则可以通过修改监听接口来实现一定程度上的安全性。
      
    - **8  关于调用OpenAI APIs的已知困难**

          由于微信APIs强制5秒的响应时间限制，而ChatGPT 4.0对于大多数prompts的响应时间都会超过这个限制，因此暂时没有办法接入OpenAI APIs。虽然Gemini也有类似的情况，但是在加入缓存机制的情况下请求失败率可以压低到10%以下，因此相对稳定。
      
    - **9  未来更新计划**
 
          1.添加接入OpenAI APIs和文言一心的兼容方法。
          2.添加微信服务器IP获取与系统防火墙白名单部署功能
          3.添加Java版本
          4.添加图文传输功能
      
