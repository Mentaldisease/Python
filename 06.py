import string,random
def func(length,lower=True,upper=True,number=True,other=True):
    lower_set = set(string.ascii_letters)
    upper_set = set(string.ascii_uppercase)
    number_set = set([x for x in range(10)])
    other_set = set(list('~!@#$%^&*()'))
    user_choice = set()
    if lower:
        user_choice = user_choice | lower_set
    if upper:
        user_choice = user_choice | upper_set
    if number:
        user_choice = user_choice | number_set
    if other:
        user_choice = user_choice | other_set
    content = random.sample(user_choice,length)
    return ''.join(content)

print(func(10,True,True))