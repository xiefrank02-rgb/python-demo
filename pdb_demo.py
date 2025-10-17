"""pdb_demo.py

演示如何在 Python 中使用 pdb 调试器的示例文件。

本文件包含：
- 递归与迭代实现的阶乘函数
- 一个在需要时触发 pdb 的调试示例（通过命令行 --debug）
- 一个带异常演示的示例，展示如何在异常发生后使用 pdb.post_mortem()
- 一个简单的类 `Calculator`，用于展示方法与异常处理
- 一个生成器示例：斐波那契数列

默认运行不会进入交互式调试；要观察 pdb 行为，请使用 --debug 标志。
"""

import argparse
import pdb
import sys
import traceback


def factorial_recursive(n: int) -> int:
    """递归计算 n 的阶乘。

    Args:
        n: 正整数

    Returns:
        n 的阶乘

    说明：这是一个简单的递归实现。对于较大的 n 会导致递归深度增大。
    """
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:
    """迭代计算阶乘，避免递归深度问题。"""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial_debug(n: int, debug_at: int = 2):
    """带可选断点的阶乘示例。

    当计算到某个中间值（debug_at）时，会调用 pdb.set_trace() 进入交互式调试。
    该函数只应在明确想要手动调试时使用（例如通过命令行 --debug 触发）。
    """
    if n <= 1:
        return 1
    if n == debug_at:
        # 在这里可以检查局部变量、调用栈等。
        # 注意：如果在非交互环境（如 CI）运行，此调用会阻塞程序。
        pdb.set_trace()
    return n * factorial_debug(n - 1, debug_at)


class Calculator:
    """示例类：包含一些基础运算方法，并演示异常触发时的调试用法。"""

    def divide(self, a: float, b: float, debug_on_zero: bool = False) -> float:
        """执行除法，若除数为 0，则抛出 ZeroDivisionError。

        若 debug_on_zero 为 True，则在检测到 b==0 时触发 pdb 以便交互式检查。
        """
        if b == 0:
            if debug_on_zero:
                pdb.set_trace()
            raise ZeroDivisionError("除数不能为 0")
        return a / b


def fibonacci_generator(n: int):
    """生成前 n 个斐波那契数的生成器示例。"""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def demo_post_mortem():
    """演示如何在捕获异常后使用 pdb.post_mortem() 进行事后调试。

    注意：post_mortem 会在异常的回溯位置打开调试器，适合在调试崩溃时使用。
    """
    try:
        # 故意触发一个异常以演示 post_mortem
        calc = Calculator()
        calc.divide(1, 0)
    except Exception:
        print("捕获到异常，进入 post-mortem 调试（如果 --debug 标志启用，会进入 pdb）")
        # 打印回溯信息以便在非交互情况下也能看到错误位置
        traceback.print_exc()
        # 在需要交互式调试时可以取消注释下一行：
        # pdb.post_mortem()


def parse_args():
    p = argparse.ArgumentParser(description="pdb 使用示例脚本")
    p.add_argument("--debug", action="store_true", help="在示例中触发 pdb 调试点")
    return p.parse_args()


def main():
    args = parse_args()

    print("示例：递归阶乘(5) ->", factorial_recursive(5))
    print("示例：迭代阶乘(5) ->", factorial_iterative(5))

    print("示例：斐波那契前 10 项 ->", list(fibonacci_generator(10)))

    # Calculator 示例
    calc = Calculator()
    print("示例：Calculator.divide(10, 2) ->", calc.divide(10, 2))

    # 当用户要求 debug 时，运行带断点的函数与 post_mortem 演示。
    if args.debug:
        print("--debug 已启用：将触发带断点的阶乘（在 n==2 时）")
        # 下面调用会在递归到指定层级时进入 pdb
        print("带断点的递归阶乘(5) ->", factorial_debug(5, debug_at=2))

        # 演示在异常发生后的 post-mortem（需要手动取消注释 pdb.post_mortem()）
        demo_post_mortem()
    else:
        print("未启用 --debug；已跳过交互式调试点")


if __name__ == "__main__":
    main()