# A product of all positive numbers less than or equal to the number e.g 4!- 4*3*2*1

def fact(num):
    if num ==1:
        return num
    else:
        return num * fact(num-1)
print(fact(6))