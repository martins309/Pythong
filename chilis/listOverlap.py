#write a program that returns a list of the most common elements without returning the duplicates
#program must work on two lists that are of different size 
#for extras:
#randomly generete two lists to test this and write it one line
#what we want it to say is [1, 3, 6, 8]

def listOverlap():
    list1 = [1,2,3,3,3,4,5,6,6]
    list2 = [1,1,1,1,2,3,4,5,6,7,8,8,8]
    
    newList = []
    newList2 = []
    
    # for a in list1:
    #     if list1.count(a) > 1:
    #         newList.append(a)
    #         print(set(newList))
    for b in list2:
        if list2.count(b) > 1:
            newList2.append(b)
            print(set(newList2))
listOverlap()
