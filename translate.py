import time
import tkinter as tk
import requests
import pyperclip
import hashlib
import random

# 设置你的百度翻译 API Key 和 Secret Key
APP_ID = 'your_baidu_app_id'  # 替换成你申请的 App ID
SECRET_KEY = 'your_baidu_secret_key'  # 替换成你申请的 Secret Key

# 百度翻译 API 地址
BAIDU_TRANSLATE_URL = "https://fanyi-api.baidu.com/api/trans/vip/translate"

# 百度翻译的签名生成方法
def generate_sign(query):
    salt = random.randint(32768, 65536)
    sign = APP_ID + query + str(salt) + SECRET_KEY
    sign = hashlib.md5(sign.encode('utf-8')).hexdigest()
    return sign, salt

# 使用百度翻译 API 进行翻译
def translate_text(text, target_lang='en'):
    query = text
    sign, salt = generate_sign(query)
    
    params = {
        'q': query,
        'from': 'auto',  # 自动检测源语言
        'to': target_lang,  # 目标语言
        'appid': APP_ID,
        'salt': salt,
        'sign': sign,
    }
    
    response = requests.post(BAIDU_TRANSLATE_URL, data=params)
    result = response.json()

    if 'trans_result' in result:
        return result['trans_result'][0]['dst']
    else:
        return "Error: Unable to fetch translation."

# 创建翻译窗口
def show_translation_window(text):
    window = tk.Tk()
    window.title("Translation")
    window.geometry("300x100+100+100")
    label = tk.Label(window, text=text, font=("Arial", 14))
    label.pack(expand=True)
    window.after(3000, window.destroy)  # 3秒后自动关闭窗口
    window.mainloop()

# 检查剪贴板内容并翻译
def monitor_clipboard():
    previous_clipboard = ""
    
    while True:
        current_clipboard = pyperclip.paste()  # 获取当前剪贴板内容
        if current_clipboard != previous_clipboard:  # 如果剪贴板内容变化
            previous_clipboard = current_clipboard
            if current_clipboard.strip():  # 如果剪贴板内容不为空
                translated_text = translate_text(current_clipboard.strip(), target_lang='en')
                show_translation_window(f"Original: {current_clipboard}\nTranslated: {translated_text}")
        time.sleep(1)  # 每秒检查一次剪贴板

# 开始监听剪贴板内容
monitor_clipboard()
