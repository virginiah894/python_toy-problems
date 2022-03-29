Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them 
the year that they will turn 100 years old.
# hardcoded year
def aging():
    x =input ('What is your name?')
    y = int(input('What is your age?'))
    turn = (2020 -y) + 100
    print(f'Hello {x}, youll will turn 100 years in : {turn}')
aging()

# Reusable

import datetime
now = datetime.datetime.now()
current_year = now.year
name = input('Enter your name')
age =int((input('Enter your age')))

when_100 = (current_year-age) +100
print(f'Hi {name}, You will turn 100 years in  {when_100}')