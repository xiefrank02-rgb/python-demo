if __name__ == "__main__":
    # 示例地址字符串，包含各种特殊字符
    test_address = (
        "123\u200B Main\u00A0Street\x01 Apt\t42B\n"
        "Springfield\r\nUSA"
    )
    print(test_address)