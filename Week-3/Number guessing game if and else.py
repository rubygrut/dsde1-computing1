#This program sees if a number guessed is equal to a number randomly generated
guess=input('Choose a number between 1 and 10:')
import random
if guess==random.randint(1,10):
    print(True)
else:
    guess=input('Choose a number between 1 and 10:')
if guess==random.randint(1,10):
    print(True)
else: 
    guess=input('Choose a number between 1 and 10:')
if guess==random.randint(1,10):
    print(True)