# -*- coding: utf-8 -*-

# This code shows an example of text translation from English to Simplified-Chinese.
# This code runs on Python 2.7.x and Python 3.x.
# You may install `requests` to run this code: pip install requests
# Please refer to `https://api.fanyi.baidu.com/doc/21` for complete api document

from ast import main
import requests
import json

from dotenv import load_dotenv
import os

# 加载 .env 文件中的环境变量
load_dotenv()

APP_ID = os.getenv('BAIDU_API_KEY')
SECRET_KEY = os.getenv('BAIDU_SECRET_KEY')

if not APP_ID or not SECRET_KEY:
    raise ValueError("API key or Secret key not found in .env file.")



def get_access_token():
    
    """使用 AK 和 SK 生成鉴权签名（Access Token）"""
    url = f'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={APP_ID}&client_secret={SECRET_KEY}'
    request = requests.post(url)
    return request.json().get('access_token')



if __name__ == '__main__':
    token = get_access_token()
    url = r'https://aip.baidubce.com/rpc/2.0/mt/texttrans/v1?access_token=' + token

    q = 'hello,world!' # example: hello
    # For list of language codes, please refer to `https://ai.baidu.com/ai-doc/MT/4kqryjku9#语种列表`
    from_lang = 'en' # example: en
    to_lang = 'zh' # example: zh
    term_ids = '' # 术语库id，多个逗号隔开

    # Build request
    headers = {'Content-Type': 'application/json'}
    payload = {'q': q, 'from': from_lang, 'to': to_lang, 'termIds' : term_ids}

    # Send request
    r = requests.post(url, params=payload, headers=headers)
    result = r.json()

    # Show response
    print(json.dumps(result, indent=4, ensure_ascii=False))




