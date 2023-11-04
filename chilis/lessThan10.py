# Take a list, say for example this one:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

# Extras:

# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.


# def lessThan5(array):
#     print([x for x in array if x<5])

# lessThan5([1, 3, 6, 5, 4, 33, 342, 3, 64, 4])


def smallerThanFive():
    oldList = [1,2,23,3,4,5,6,7,8]
    newList = []
    otherList = []
    
    for o in oldList:
        if o < 5:
            newList.append(o)
    print(newList)
    print()
    
    user = int(input("you know what i wnat ;) :  "))
    for old in oldList:
        if old < user:
            otherList.append(old)
            otherList.sort()
    print(otherList)
smallerThanFive()