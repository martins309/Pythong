
import time 

name = input("What is your name?")
print("hello," + name, "Its show time")

time.sleep(1)

print("start guessing")
time.sleep(0.5)

word = "chicken"

guesses = ''
turns = 10

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
