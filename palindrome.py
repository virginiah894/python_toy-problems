
# Ask the user for a string and print out whether this string is
#  a palindrome or not.
#  (A palindrome is a string that reads 
#  the same forwards and backward


def palindrome():
     word =input("Write a string here")
     opp= word[::-1]
     if word == opp:
         print('palindrom')
     else:
         print('Not a palindrom')
palindrome()

