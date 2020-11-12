import sys
import random 
def guess():
    n = random. randint(0,10)
    x = int(input('Guess a number'))
    while x!= n:
        if x <  n:
            print('Too Low')
            x = int(input('Guess a number'))
        elif x > n:
            print('Too High')
            x = int(input('Guess a number'))
       
            
    else:
        print('Exactly Right')
        sys.exit()
guess()