def greet(name: str) -> str:
    return "Hello, " + name


# 这样，即使传入 int 类型也会正常工作
print(greet(str(123)))  # 输出: Hello, 123