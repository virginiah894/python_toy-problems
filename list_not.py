Write a program (function!) that takes a list and returns a new
 list that contains all the 
elements of the first list minus all the duplicates.
Bonus point:
Write two different functions to do this - 
one using a loop and constructing a list, and another using sets.

# using sets
def unique_elements(x):
    print(set(x))
unique_elements([1,2,3,2,3,4,5,6,4,5,7,8,9])

# using lists
def unique_list(z):
    emp=[]
    for i in z:
        if i not in emp:
            emp.append(i)
    return(emp)
z=[1,2,2,4,3,3,5,5,6,7,8,9,9]
print(unique_list(z))
