#write a program that returns a list of the most common elements without returning the duplicates
#program must work on two lists that are of different size 
#for extras:
#randomly generete two lists to test this and write it one line


def listOverlap():
    list1 = [1,2,3,3,3,4,5,6,6]
    list2 = [1,1,1,1,2,3,4,5,6,7,8,8,8]
    
    newList = []
    
    for i in zip_longest(list1, list2):
        