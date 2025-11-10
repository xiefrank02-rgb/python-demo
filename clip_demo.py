import pyperclip
import re


def camel_to_snake(camel_str):
    # 在大写字母前加下划线，并转换成小写
    snake_str = re.sub(r'([A-Z])', r'_\1', camel_str).lower()
    # 如果字符串以下划线开始（例如：CamelCase -> _camel_case），去掉开头的下划线
    return snake_str.lstrip('_')


if __name__ == "__main__":
    # 从文件读取字段列表
    with open("words.txt", "r", encoding="utf-8") as f:
        fields = [line.strip() for line in f if line.strip()]

    # 从剪切板获取文本
    text = pyperclip.paste()

    # 按行分割文本
    lines = text.splitlines()

    # 遍历每行，检查是否包含字段
    for idx, line in enumerate(lines, start=1):
        for field in fields:
            if camel_to_snake(field) in line:
                print(f"Line {idx}: {line}")
                break  # 一行匹配多个字段，只打印一次