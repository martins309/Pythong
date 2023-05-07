#import time module
import time 

#get the user input
name = input("What is your name?")
print("hello," + name, "Its show time")

#wait one second
time.sleep(1)

#print statement to prompt the user to guess the word
print("start guessing")
time.sleep(0.5)

#set word 
word = "chicken"

#set the guesses to an empty string
guesses = ''

#set the number of turns
turns = 10

#create a while loop
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end="")
        else:
            print("_",end="")
            failed += 1
    if failed == 0:
        print("you won!!")
        break
    guess = input(" guess a character:")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("that is incorrect")
        print("you have,", turns, "more guesses")

        if turns ==  0:
            print("you suck")
