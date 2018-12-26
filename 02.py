from functools import reduce
def sum(lst):
    return reduce(lambda x,y:x+y,lst)

print(sum([1,2,3,4,5]))