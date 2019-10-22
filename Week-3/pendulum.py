import math
L = int(input('Give me the length of the pendulum:')
if ValueError:
    print('That is not a number!')
g=int(input('What is the gravity:'))
T=int((2*math.pi) * math.sqrt(L/g))
def period(T):
    T=(2*math.pi) * math.sqrt(L/g)
    return T
print('The period T of a friction-less pendulum is:' + str(period(T)))
