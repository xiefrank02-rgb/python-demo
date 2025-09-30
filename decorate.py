from functools import wraps

def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return wrapper



@debug
def hello(name):
    return "Hello " + name

hello("Bob")