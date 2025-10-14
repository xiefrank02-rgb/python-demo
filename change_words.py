# -*- coding: utf-8 -*-
"""
为单词添加前后缀
""" 
import re


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

    # 生成新的单词列表
    # new_words = [f"<{word}>{{{{word}}}}</{word}>" for word in words]
    new_words = [f"<{word}>{{{{{word}}}}}</{word}>" for word in words]
    
    # 输出结果
    for _, new_word in zip(words, new_words):
        print(f"{new_word}")


if __name__ == "__main__":
    word_file = 'words.txt'  # 包含要查找的单词的文件
    change_words(word_file, '"', '",')  # words.txt 
    print("\n")
    custom_words(word_file)