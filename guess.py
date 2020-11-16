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

# counts the number of tries
# counting is abit off

import random
random_num = random.choice(range(1,10))
tries = 0
count = 0
user_guess = []

while user_guess != "exit":
    user_guess = input("Guess a number between 1 and 9 or enter 'exit' to quit: ")
    if user_guess == "exit":
        print("Game over, you were right", count, "times after", tries, "tries.")
    elif int(user_guess) == random_num:
        count += 1
        print("Exactly right")
    elif int(user_guess) < random_num:
        print("Too low")
    elif int(user_guess) > random_num:
        print("Too high")
        tries += 1
        continue


# Adds a counter that checks the number of tries
import random

gene_num = random.randint(1,9)
user_guess = 0
counter = 0
while user_guess != gene_num and user_guess != "exit":
    user_guess = input("Pick a random number between 1 and 9 or type 'exit' to quit ?")
    
    if user_guess == "exit":
        print("You have taken",counter,"tries!")
        
        break
    
    user_guess = int(user_guess)
    counter += 1
    
    if user_guess < gene_num:
        print("Too low!")
    elif user_guess > gene_num:
        print("Too high!")
    else:
        print("Exactly right!")
        print("After",counter,"tries!")