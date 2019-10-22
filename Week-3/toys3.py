a= int(input('Enter a numero:'))
b=int(input('Give me another numero:'))
def inc_return(a):
    product = a+1
    return product
print('Your first number plus one is:' + str(inc_return(a)))

# write a function that adds
# the two input numbers together
# and returns the sum

def sum(a, b):
    sum = a+b
    return sum
print('Your first number plus your second number is:'+str(sum(a, b)))

# write a function that takes two
# numbers, adds them together using 
# sum() and then increments the sum
# using inc_return

def inc_return(a, b):
    inc_return = a+b+1
    return inc_return
print('Your first number plus the second incremented by 1 is:' + str(inc_return(a, b)))

# write a function that returns a 
# boolean (True or False) for whether 
# the input number is even

c=int(input('Ay up give me an even number:'))
def if_even(c):
    if c%2==0:
        return True
    else:
        return False
if if_even(c)==True:
    print('Well done you')
else:
    print('Bad try')

# create for loop that takes a string
# and an integer and returns a new string 
# that is the string repeated equal to 
# integer
# e.g. string_repeat('ho', 3) returns
# 'hohoho'

d = str(input('Tell me a short phrase:'))
e = int(input('Give me a number less than 10:'))
def string_repeat(d, e):
    product = d * e
    return product
print('Your phrase repeated as many times as your number is:' + string_repeat(d, e))



