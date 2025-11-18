import requests

def check(resp,word):
    result = word.lower() in resp.lower()
    print(word,result)

def find_and_print_lines(text, keyword):
    """
    检查文本中是否包含指定关键字，并打印包含该关键字的所有行
    
    参数:
        text (str): 要检查的文本（可包含换行符）
        keyword (str): 要搜索的关键字
    """
    # 按行分割文本
    lines = text.split('\n')
    
    # 遍历每一行
    for line_num, line in enumerate(lines, 1):  # 从1开始计数行号
        # 检查关键字是否在当前行中（不区分大小写）
        if keyword.lower() in line.lower():
            print(f"第{line_num}行: {line}")

def find_keys_and_print(keys, keyword):
        for key in keys:
            if keyword.lower() in key.lower():
                print(key)

if __name__ == "__main__":
    url = 'http://fat-irs.juanhandapi.com/api/getDefinedVars'
    response = requests.get(url)
    # resp_text = response.text
    # print(response.status_code)
    # print(response.text)
    # with open("check_words.txt", 'r', encoding='utf-8') as f:
    #     words = [w.strip() for w in f if w.strip()]  # 去除空行与换行符
    # for word in words:
    #     check(resp_text,word)
    resp_json = response.json()
    with open("find_vars.txt", 'r', encoding='utf-8') as f:
        words = [w.strip() for w in f if w.strip()]  # 去除空行与换行符
    for word in words:
        find_keys_and_print(resp_json.keys(),word)
