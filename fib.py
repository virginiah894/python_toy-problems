# method one
v = int(input("How many fibonacci numbers do you want to generate?"))
   
def fibonacci(x):
        v, p = 0, 1
        for _ in range(x):
            yield v
            #  update the nth index to add the previous
            v, p = p, v+p
print(list(fibonacci(v)))


fibonacci(7)


# try 2
x = int(input('Enter your length'))
print('\n')
def Fibo():
    a=firnum=0
    b=1
    while firnum<x:
        print(a)
    #   finds the next indexes
        firnum=firnum+ 1
        # sums the previous numbers 
        newtot=a+b
        a=b
        b=newtot
        
Fibo()

