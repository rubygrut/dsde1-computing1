def inc(a):
    float(a)    
    a=a+1
    print(a)

def inc_return(d):
    float(d)
    d=d+1
    return(d)

# write a function that adds
# the two input numbers together
# and returns the sum

def sum(a, b):
    int(a)
    int(b)
    c= a +b
    return(c)

# write a function that takes two
# numbers, adds them together using 
# sum() and then increments the sum
# using inc_return

def sum_inc(a, b):
    int(a)
    int(b)
    c=a+b
    d=inc_return(c)
    return(d)

# write a function that returns a 
# boolean (True or False) for whether 
# the input number is even

def is_even(a):
    b=(a%2==0)
    return(b)

# create for loop that takes a string
# and an integer and returns a new string 
# that is the string repeated equal to 
# integer
# e.g. string_repeat('ho', 3) returns
# 'hohoho'

def string_repeat(phrase, repeat):
    str(phrase)
    int(repeat)
    return(phrase * repeat)