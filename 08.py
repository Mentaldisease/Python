import time
def do(fn):
    def wrapper(*args,**kwargs):
        start = time.time()
        rs = fn(*args, **kwargs)
        end = time.time()
        print(end - start)
        return rs
    return wrapper

@do
def func():
    for i in range(2000):
        print(i)

func()