def my_gen(num):
    x = open('note.txt','r')
    while 1:
        yield x.read(num)

g = my_gen(15)
print(next(g))
print(next(g))

