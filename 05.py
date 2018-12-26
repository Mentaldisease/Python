def fib(n):
    if n <= 1:
        return 1
    else:
        return(fib(n-1)+fib(n-2))


for x in range(10):
    if fib(x) < 10:
        print(fib(x))