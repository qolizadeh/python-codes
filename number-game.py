
# Developed by "Reza Heiadrgholizadeh"

import random
import os

############################################

############################################

# main

# loop try again
while True:

    # loop get number prediction
    while True:
        n = int(input("The number of predictions that you want to guess:"))
        if (n > 0):
            break
        continue

    # loop get minimum number
    while True:
        minimum = int(input("Enter the Number Minimum ---- > Minimum >= 0:"))
        if (minimum < 0):
            print("you enter Minimum <0 (Minimum your = {})".format(minimum))
            continue
        break

    # loop get maximum number
    while True:
        maximum = int(input("Enter the Number Maximum ---- > Maximum > Minimum:"))
        if (minimum > maximum):
            print("you enter Maximum < Minimum (Maximum your = {})".format(maximum))
            continue
        break

    num = random.randint(minimum, maximum)
    print(num)

    flag = False
    # loop number prediction
    for _ in range(n):
        forcast = int(input("forecasting you from Number:"))
        if ( forcast == num ):
            flag = True
            break
        elif (forcast > num):
            print("random number < {}".format(forcast))
        elif (forcast < num):
            print("random number > {}".format(forcast))
        else:
            print("number({}) input is not valid.".format(forcast))

    # loop get [Y/N]
    while True:
        if (flag):
            print("You won the game.")
        else:
            print("You missed the game.")

        try_again = str(input("You want to play again[Y/N]:"))
        if ( try_again.lower() == "y"):
            os.system('cls' if (os.name == 'nt') else 'clear')
            break
        elif (try_again.lower() == "n"):
            exit(0)
        else:
            print("Error: string input is not valid.")