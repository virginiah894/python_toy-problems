#  Armstrong number - number where the  sum of the cube of digits make the number eg 153
num = int(input('Enter a number '))
# sum is initialized at 0
sum_num = 0
# sum of cube of each digit
temp =num
while temp >0:
    digit = temp % 10
    sum_num += digit **3

    # Floor operator to return the number to the nearest lower whole number
    temp //= 10
if num == sum_num:
         print('This is an armstrong number')
else:
        print('Not an armstrong')



