# Create a program that asks the user for a number 
# and then prints out a list of all the divisors of that number. 
# (If you don’t know what a divisor is, it is a number that divides evenly into another number. 
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)


 def divisor():
     div = []
     y = range(10,28)
     num = int(input("gimme a number little boy:  "))
     print()
     __=input("and make it snappy or else")
     
     for el in y:
         if num % y == 0:
             div.append(num)
    print(div)