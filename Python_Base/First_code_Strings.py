## 
## first code in python is dedicated to STRINGS in python 
## This is a small compilation of how Strings work in the inner world of python 
## though it is basic but understanding this would take you on the heights you want in python because number and strings 
## are oil of this snake.

# Strings are immutable 

# Question : how to append strings n times (or concatenate n times) ?

def concat_strings(s,n):
    output = ''
    i= 0
    while i < n:
        output += s
        i +=1
    return output

H = concat_strings('trish ',4)

print(H)

# Another method using list and at the end using Join() to combine element of list:

def combine_strings(s,n):
    l =[]
    i = 0 
    while i <n:
        l.append(s)
        i +=1
    return ''.join(l)
J = combine_strings('chick ',6)
print(J)
