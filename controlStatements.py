# bonus = 20
# if bonus <= 10:
#     bonus = 100
# else:
#     bonus = 200
# print ("\n bonus = ", bonus)

# age = int(input("How old is you?: "))
# if age < 18:
#     print("You are not eligible to vote")
# else:
#     print("You are eligible to vote") 

# age = int(input("How old are you?: "))

# if age >= 65:
#     print("You are eligible to retire")
#     print("You can have a drink")
#     print("You are eligible to vote")
#     print("You can drive a car")
# elif age >= 21:
#     print("You can have a drink")
#     print("You are eligible to vote")
#     print("You can drive a car")
# elif age >=18:
#      print("You are eligible to vote")
#      print("You can drive a car")
# elif age >= 16:
#      print("You can drive a car")
# else:
#     print("You're too young to do anything so give up lol")
#     print("Sorry not sorry")


# bonus = 55
# if bonus <= 15:
#     num = 100
# else:
#     num = 200
# print("\n num = ", num)

# years = int(input("Enter the number of years you've been married: "))
# if years == 1:
#     print("Your first year -- great")
# elif years == 10:
#     print("A whole decade -- impressive")
# elif years == 25:
#     print("your sikver anniversary -- enjoy")
# elif years == 50:
#     print("your golden anniversary")
# else:
#     print("pffft")

#Logical operators and, or, not
# operator priority ranking: 1st: not, 2nd: and, 3rd: or
#shows which one of these operators will be evaluated first

# age = int(input("Enter your age: "))
# city = input("Enter your city (Newark or other): ")


# #AND operator
# if age >= 65 and city == "Newark":
#     print("\nYou are over 64 and live in Newark. ")
# else: 
#     print("\nYour are", age, "and live in", city)

# #/****************************************************
# age = int(input("Enter your age: "))

# #OR operator
# if age >=65 or age <= 18:
#     print("You are", age, "years old")
# else:
#     print("You are between 19 and 64. ")

# #/****************************************************
age = int(input("Enter your age: "))

# NOT operator
if not age <= 21:
    print("You are", age, "years old")
    print("You are older than 21")
else:
    print("You are age", age, "years old")
    print("You are under 21")


