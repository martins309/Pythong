#This is the absolute value function 
# number = -209
# print("the absolue value of this number is : ", abs(number))


# the all method returns True when all elements in the given iterable are true

# q = [1,2,3,4,5,6]
# print(all(q))

# x = [1, 0]
# print(all(x))

# w = [3,False,0]
# print(all(w))

# o =[]
# print(all(o))

#This is an example of a recursive fuction 

def cal_factorial(x):
    if x == 1:
        return 1
    else:
        return (x * cal_factorial(x-1))
num = 10
print("The factorial of", num, "is", cal_factorial(num))

#This is a lamba function
#synonymous with anonymous function
chicken = lambda q: q * 12 - abs(-3674)
print("THis is lambda: ", chicken(3))


