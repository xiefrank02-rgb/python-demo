from utils  import string_utils


if __name__ == "__main__":
    with open("words.txt", 'r', encoding='utf-8') as f:
        words = [w.strip() for w in f if w.strip()]  # 去除空行与换行符
    for word in words:
        string_utils.camel_to_snake(word)