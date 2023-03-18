#Feel free to add another riddle if you want to.
que = input("Do you wanna hear a riddle? ")
if que == "yes":
    #def main():
    def real():
        guess = 7
        quno = input("Everybody falls for me, even you. What am I?").lower()
        if quno == 'gravity':
            print(quno," correct!")
        else:
            guess -= 1
            print(f"You have {guess} lives left.")

        qdos = input("What time is it when an elephant sits on a fence? ").lower()
        if qdos == 'time to get a new fence':
            print("Bazhinga!")
        else:
            guess -= 1
            print(f"You have {guess} lives left.")

        qtres = input("What do you call a nose that's 12 inches long? ")
        if qtres == 'a foot':
            print("A stinky foot, you mean.")
        else:
            guess -= 1
            print(f"You have {guess} lives left.")

        qatres = input("What can you catch but never throw?")
        if qatres == 'cold':
            print("I think I'm coming down with a case of the shnifles.")
        else:
            guess -= 1
            print(f"You have {guess} lives left.")

        quince = input("What belongs to you but is used by everyone you meet?")
        if quince == 'name':
            print("Your name, dumdum.")
        else:
            guess -= 1
            print(f"The answer was name. You have {guess} lives left.")
        if guess == 0:
            print("You need to build yourself intellectually.")
        elif guess != 0:
            print("Best play with your cards close to your chest")

    real()















































    
