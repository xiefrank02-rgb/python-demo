import re
from functools import wraps

def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # print('Running function:', func.__name__)
        # print('Positional arguments:', args)
        # print('keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print(result)
        return result
    return wrapper

@debug
def snake_to_camel(snake_str):
    """
    将下划线命名的字符串转换为驼峰命名
    
    参数:
        snake_str: 下划线分隔的字符串，如 "loan_purpose_code"
        
    返回:
        驼峰命名的字符串，如 "loanPurposeCode"
    """
    # 分割字符串为单词列表
    words = snake_str.split('_')
    
    # 如果字符串为空或只包含下划线，返回空字符串
    if not words or all(word == '' for word in words):
        return ''
    
    # 第一个单词保持小写，后续单词首字母大写
    camel_case = words[0].lower() + ''.join(word.capitalize() for word in words[1:])
    
    return camel_case

@debug
def camel_to_snake(camel_str):
    # 在大写字母前加下划线，并转换成小写
    snake_str = re.sub(r'([A-Z])', r'_\1', camel_str).lower()
    # 如果字符串以下划线开始（例如：CamelCase -> _camel_case），去掉开头的下划线
    return snake_str.lstrip('_')