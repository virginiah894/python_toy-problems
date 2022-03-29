 Write a function that takes in an integer and generates 
 all the prime numbers between 0 and the input integer. 
 Then write another function that asks the user for a number and 
 determine whether the number is prime or not.


def prime(x,y):
    for num in range(x,y+1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)
prime(1,20)


# determines if number is prime or not


def true_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True             
print(true_prime(5))