# Write a password generator in Python. 
# Be creative with how you generate passwords 
# - strong passwords have a mix of lowercase letters, 
# uppercase letters, 
# numbers, and symbols. The passwords should be random, generating 
# a new password every time the user asks for a new password.
#  Include your run-time code in a main method.
# Bonus point:
# Ask the user how strong they want their password to be.
#  For weak passwords, pick a word or two from a list.

#  generates password only
import random, string
def strong_password():
    question = int(input('How Long do you want your password?'))
    gen_pass = string.ascii_letters + string.digits + string.punctuation
    empty = []
    for i in range(question):
        empty.append(random.choice(gen_pass))
    print(''.join(empty))
strong_password()