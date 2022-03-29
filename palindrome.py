# Checks if a string is a palindrome on 

def palindrome(num):
    rev = num[::-1]
    if rev ==num:
        print('Is Palindrome')
    else:
        print('Not Palindrome')
palindrome('gytes')