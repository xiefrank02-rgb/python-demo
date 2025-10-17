# -*- coding: utf-8 -*-
"""
为单词添加前后缀
""" 
import re

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



def change_words(word_file, prefix, suffix):
    # 读取单词列表
    with open(word_file, 'r', encoding='utf-8') as f:
        words = [w.strip() for w in f if w.strip()]  # 去除空行与换行符

    # 生成新的单词列表
    new_words = [f"{prefix}{word}{suffix}" for word in words]

    # 输出结果
    for _, new_word in zip(words, new_words):
        print(f"{new_word}")

def custom_words(word_file):
    # 读取单词列表
    with open(word_file, 'r', encoding='utf-8') as f:
        words = [w.strip() for w in f if w.strip()]  # 去除空行与换行符

    words_snake = [print(snake_to_camel(word)) for word in words]
    # 生成新的单词列表
    # new_words = [f"<{word}>{{{{word}}}}</{word}>" for word in words]
    new_words = [f"<{snake_to_camel(word)}>{{{{{word}}}}}</{snake_to_camel(word)}>" for word in words]
    
    
    
    # 输出结果
    for _, new_word in zip(words, new_words):
        print(f"{new_word}")


if __name__ == "__main__":
    word_file = 'words.txt'  # 包含要查找的单词的文件
    change_words(word_file, '"', '",')  # words.txt 
    print("\n")
    custom_words(word_file)