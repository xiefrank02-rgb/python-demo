def decorate_it(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        ret = func(*args, **kwargs)
        print("After function call")
        return ret
    return wrapper

@decorate_it
def hello(name):
    print("Hello,", name)
    return name


if __name__ == "__main__":
    name = hello("Alice")
    print("Returned:", name)