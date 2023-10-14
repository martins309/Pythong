# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

# Extras:

# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.







def evenOdd():
    user = int(input("Pick a number between 1 and 10:  "))
    if user % 4 == 0:
        print("no this wont do either, this is divisble by 4")
    elif user % 2 == 0:
        print("I don't like this, it's an even number")
    else:
        print("wtf this one an odd number ><")
    print()
    _= input("alright pick two numbers now")
    check = int(input("okay pick the first number:  "))
    div = int(input("Okay now pick the second number:  "))
    
    if check % div == 0:
        print("okay this works because there is no remainder")
    else:
        print("nope try that again")
   
            

evenOdd()