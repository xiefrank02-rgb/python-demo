# 从 time 模块导入 perf_counter，用于高精度计时
from time import perf_counter 
# 从 functools 模块导入 wraps，用于在装饰器中保留原始函数的元信息（如函数名、文档字符串）
from functools import wraps

def timer(func):
    """
    一个装饰器函数，用于测量被装饰函数的执行时间。
    """
    # @wraps(func) 是一个重要的步骤，它会将 wrapper 函数的一些属性（如 __name__, __doc__）
    # 设置为与 func 函数相同，这样在调试或打印函数信息时就能得到正确的原始函数信息。
    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        包裹函数，负责在调用原函数前后计时。
        *args 和 **kwargs 是特殊语法，用于接收任意数量的位置参数和关键字参数，
        确保装饰器可以适用于任何签名的函数。
        """
        # 记录函数开始执行时的时间戳
        start = perf_counter()
        
        # 调用原始函数，并将接收到的所有参数（*args, **kwargs）传递给它
        # 同时保存函数的返回值
        result = func(*args, **kwargs)
        
        # 记录函数执行结束时的时间戳
        end = perf_counter()
        
        # 计算并打印函数名、传入的参数以及总耗时
        # 使用 f-string 进行格式化输出，更加简洁易读
        print(f"Function '{func.__name__}'({args}, {kwargs}) finished in {end - start:.6f} secs")
        
        # 返回原始函数的执行结果，保证装饰器不会改变函数的行为
        return result
        
    # 返回包裹函数 wrapper
    return wrapper

@timer
def countdown(n):
    """
    一个简单的倒计时函数，通过 while 循环从 n 递减到 0。
    这是一个时间复杂度为 O(n) 的算法，因为其运行时间与输入 n 的大小成正比。
    """
    while n > 0:
        n -= 1

# 这是Python的标准执行入口。
# 当这个脚本文件被直接运行时，__name__ 变量的值会被设置为 "__main__"，
# 此时 if 条件成立，下面的代码块就会被执行。
# 如果这个文件被其他脚本作为模块导入（例如：import my_script），
# 那么 __name__ 的值将是模块名（"my_script"），if 条件不成立，代码块就不会执行。
if __name__ == "__main__":
    # --- 开始执行主程序 ---
    print("--- Starting performance tests ---")

    # 第一次调用：测试小规模输入
    countdown(100000)
    # 预期输出类似: Function 'countdown'((100000,), {}) finished in 0.005123 secs

    # 第二次调用：测试大规模输入
    countdown(10000000)
    # 预期输出类似: Function 'countdown'((10000000,), {}) finished in 0.178456 secs
    
    print("--- Tests finished ---")