#Guessing Game One

import random
attempt = 0

number = random.randint(2,9)

while True:
    inNum = int(input('guess a number\n'))
    attempt += 1
    if inNum == number:
        print("Correct\nYou got it on attempt number: %i"%(attempt))
    elif inNum < number:
        print("too low")
    else:
        print("too high")
    user = input("Type quit to quit. To keep going press enter\n")
    if 'quit' in user: break