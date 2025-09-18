




if __name__ == "__main__":
    test_case = ["123", "abc", "45.67", "", "0", "-100"]
    for case in test_case:
        try:
            res = int(case)  # 尝试将字符串转换为整数
        except ValueError:
            pass 
        print(f"Input: '{case}' => Output: {res}")