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

# Another method using list and at the end using Join() to combine element of list:

def combine_strings(s,n):
    l =[]
    i = 0 
    while i <n:
        l.append(s)
        i +=1
    return ''.join(l)
J = combine_strings('chick ',6)


# Question 2: 
#  Reverse the string using for loop 

def reverse_string(input_string):
    output_string = ''
    for i in input_string:
        output_string = i + output_string # checkout we are reversing the order of printing variables here!!
    return output_string
ex1 = 'I am  Lord Voldemort.'
K = reverse_string(ex1)

#  Reverse the string using Slicing :

def reverse_slice(str1):
    return str1[::-1] # consider the indexing rule as start:stop:step where -1 step is reverse

L = reverse_slice(ex1)

# Reversing the string using While Loop   :
def reverse_while(str1):
    ln =len(str1)-1
    s = ""
    while ( ln >= 0):
        s += str1[ln]
        ln = ln-1
    return s
M = reverse_while(ex1)

# Reversing the string using Join and Revere method (In-build) :

def reverse_join_rev(str1):
    return ''.join(reversed(str1))
N = reverse_join_rev(ex1)

# Reversing String using Recursion 

def reverse_recurr(str1):
    if len(str1) == 0:
        return str1
    else:
        return reverse_recurr(str1[1:])+str1[0]
P = reverse_recurr(ex1)



if __name__ == "__main__":
    print("\n String Append Using + :: ", H)
    print("\n String Append Using Join() method:: ",J )
    print("\n Reversing String using For loop ::",K)
    print("\n Reversing String using Slicing ::", L)
    print("\n Reversing String using while loop ::", L)
    print("\n Reversing String using join and Reverse method ::", N)
    print("\n Reversing String using using Recursion  ::", P,end= '\n')

