# -*- coding: utf-8 -*-
"""
查找单词在目标文件中的位置
""" 
import re


def find_word_in_file(word_file, target_file):
    # 读取单词列表
    with open(word_file, 'r', encoding='utf-8') as f:
        words = [w.strip() for w in f if w.strip()]  # 去除空行与换行符

    # 读取目标文件
    with open(target_file, 'r', encoding='utf-8') as f:
        target_lines = f.readlines()

    # 遍历每个要查找的单词
    for word in words:
        found = False
        word_lower = word.lower()  # 小写匹配

        # 遍历目标文件的每一行
        for line_num, line in enumerate(target_lines, start=1):
            # 按非空字符拆分成“单元”，如 adaptiveEducation
            words_in_line = re.findall(r'\S+', line)

            # 遍历每个“单元”，查找包含关系
            for col_num, token in enumerate(words_in_line, start=1):
                if word_lower in token.lower():  # 模糊匹配，不区分大小写
                    print(f"{word} {line_num}:{col_num}")
                    found = True
                    break

            if found:
                break

        # 没找到则输出 NAN
        if not found:
            print(f"{word} NAN")


if __name__ == "__main__":
    word_file = 'words.txt'  # 包含要查找的单词的文件
    # target_file = r"\\wsl.localhost\Ubuntu\home\xiefu01\repos\phiRisk\service\risk_flow\varsCalculation\antifraud_config.py"
    # find_word_in_file(word_file, target_file)
    # print("****"*10)
    target_file = r"\\wsl.localhost\Ubuntu\home\xiefu01\repos\phiRisk\service\risk_flow\droolsCalculation\jinjaDroolsTemplate\PhiLimitNew.xml"

    find_word_in_file(word_file, target_file)
    print("****"*10)
    target_file = r"\\wsl.localhost\Ubuntu\home\xiefu01\repos\phiRisk\service\risk_flow\droolsCalculation\smt_drools_limit_new.py"
    # target_file = r"\\wsl.localhost\Ubuntu\home\xiefu01\repos\phiRisk\service\risk_flow\droolsCalculation\ttcash_drools_limit_new.py"
    find_word_in_file(word_file, target_file)