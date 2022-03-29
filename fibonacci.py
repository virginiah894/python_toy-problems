# A series of numbers where  each number is the sum of two preceding numbers e.g 0,1,1,2,3,5,8,13

# method one
v = int(input("How many elements do you want to generate ? "))
   
def fibonacci(x):
        v, p = 0, 1
        for i in range(x):
            yield v
            #  update the nth index to add the previous
            v, p = p, v+p
print(list(fibonacci(v)))






#    Method2 # 

# a =int(input('Enter a first number '))
# b = int(input('Enter a second number  '))
# n = int (input('Enter a number of elements '))
# print(a, b, end=" " +"\n")
# while n-2:
#         c = a+b
#         a =b
#         b= c
#         print (c, end=" "  + "\n")
#         n = n-1
        



