import random
from hangman_Ugwuanyi import noose


print("**** Welcome to David's Hangman Game ****\n")

words = ['psychology', 'engineering', 'hospitality', 'opportunity']

picked = random.choice(words)

print(f"Hint: The word has {len(picked)} letters\n")
dash = ["_"] * len(picked)
wrong = []

print("A wrong letter increases your chances of being hanged")
noose(len(wrong))

def update():
    print(*[i for i in dash])

while True:

    guess = input("Guess a letter >>> ")

    if guess in picked:
        index = 0
        for i in picked:
            if i == guess:
                dash[index] = guess
            index += 1
        update()


    else:
        if guess not in wrong:
            wrong.append(guess)
            noose(len(wrong))
            print("Sorry, wrong letter",wrong)
        else:
            print('you already guessed that')
            print(f"Wrong letters are {wrong}")

    if len(wrong) == 9:
        print("You lose")
        break

    if "_" not in dash:
        print("Congratulations, you had it right")
        break


"""
#This is a word guessing game

import random

print("**** Welcome to David's Hangman Game ****\n")

words = ['python', 'program', 'hospital', 'opportunity']

picked = random.choice(words)
#print(picked)

print(f"Hint: The word has {len(picked)} letters")
dash = ["_"] * len(picked)
wrong = []


def update():
    print(*[i for i in dash])

while True:

    guess = input("Guess a letter >>> ")

    if guess in picked:
        index = 0
        for i in picked:
            if i == guess:
                dash[index] = guess
            index += 1
        update()


    else:
        if guess not in wrong:
            wrong.append(guess)
            print("Sorry, wrong letter",wrong)
        else:
            print('you already guessed that')
            print(f"Wrong letters are {wrong}")

    if "_" not in dash:
        print("Congratulations, you had it right")
        break

"""