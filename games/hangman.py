import time 

name = input("What is your name?")
print("hello", + name, "Its show time")

time.sleep(1)

print("start guessing")
time.sleep(0.5)

word = "chicken"

guesses = ''

while guesses > 0:
    failed = 0
    for char in guesses:
        print(char, end=""),
    else:
        print("_",end="")
    failed += 1
