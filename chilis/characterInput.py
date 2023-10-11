# write a program that asks the user their name and their age. T
# then have a message printed out to them that says when they will turn 100 years old 
# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)



# name = input("what the fuck is your name:  ")
# print("nice to meet you: ", name)

# age = int(input("how old are you again?"))
# print("are you really: ", age, "years old?")

# print(4 * "test")

name = input("what is your name?")
age = input("how old are you?")
old = 2023 - int(age)+ 100

print("Hello", name, "you are currently", age,  "years old and in: ", old, "years you will be 100")
print()
number = int(input("pick a number that is between 1 and 100: "))

if number > 100:
    print("dont do that")
else:
    print("Hello", name, "you are currently", age,  "years old and in: ", old, "years you will be 100" )