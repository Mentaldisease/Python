def has_null_value(lst):
    return all(lst)


print(has_null_value([0,0.0,'0']))

def has_null_value2(lst):
    return list(filter(None, lst)) == lst

print(has_null_value2(['0',0,'',[]]))