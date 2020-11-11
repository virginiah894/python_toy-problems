#   Take two lists, say for example these two:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the 
# elements that are common between the lists (without duplicates).
#  Make sure your program works on two lists of different sizes.

# prints a new list all while looping
def common_elements(a,b):
    newlist = []
    for i in a:
        if  i in b:
            newlist.append(i)
            print(newlist)
common_elements([1,2,3,4,5,6],[2,3,5,6])
# prints on cosole..not list
def common_elements(a,b):
    
    for i in a:
        if  i in b:
            print(i)
common_elements([1,2,3,4,5,6],[2,3,5,6])


# refactor using set intersection method

def common_elements(a,b):
    print(set(a).intersection(b) )
   
common_elements([1,2,3,4,5,6],[2,3,5,6])

# refactor 3
def common_elements(a,b):
    lst3 = [value for value in a if value in b] 
    print (lst3)
   
common_elements([1,2,3,4,5,6],[2,3,5,6]) 

# DRY
def common_elements(a,b):
  print([value for value in a if value in b]) 
common_elements([1,2,3,4,5,6,7],[2,1,5,6,7])
