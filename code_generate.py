import random
import string

def generate_complex_password(length=8):
    """
    生成一个指定长度的复杂密码
    
    参数:
        length (int): 密码长度，默认为8位
    
    返回:
        str: 生成的复杂密码字符串
        
    确保生成的密码至少包含以下四类字符各一个：
    - 大写字母
    - 小写字母
    - 数字
    - 特殊字符
    """
    # 定义各类字符集
    upper_case = string.ascii_uppercase  # 大写字母 A-Z
    lower_case = string.ascii_lowercase  # 小写字母 a-z
    digits = string.digits  # 数字 0-9
    punctuation = string.punctuation  # 特殊字符如 !@#$%^&*() 等

    # 确保密码包含每种字符类型至少一个
    password_characters = [
        random.choice(upper_case),    # 随机选择一个大写字母
        random.choice(lower_case),    # 随机选择一个小写字母
        random.choice(digits),        # 随机选择一个数字
        random.choice(punctuation)    # 随机选择一个特殊字符
    ]

    # 计算剩余需要填充的字符长度
    remaining_length = length - len(password_characters)
    
    # 组合所有字符类型
    all_characters = upper_case + lower_case + digits + punctuation
    
    # 随机选择剩余长度的字符
    password_characters += random.choices(all_characters, k=remaining_length)

    # 打乱字符顺序以增加随机性
    random.shuffle(password_characters)

    # 将字符列表连接成最终的密码字符串并返回
    return ''.join(password_characters)

# 示例：生成一个8位的复杂密码并打印
password = generate_complex_password(8)
print("Generated Password:", password)