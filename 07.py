from functools import partial
def mul_by_two(*args):
    s = 2
    for n in args:
        s = s * n
    return s

a = partial(mul_by_two)
print(mul_by_two(20))