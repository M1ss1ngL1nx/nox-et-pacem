#name = input("What is your name?>> ")
#print()
#score = float(input("What did you score?>> "))
#gradpt= score / 3.5
'''
if score > 100:
    print("Invalid score. Out of bounds!")
elif score <= 100 and score >= 80:
    print("Congrats! You got an A.")
elif score >= 70:
    print("You got a B. Well done.")
elif score <= 60 and score >= 50:
    print(f"{score}%, An average C.")
elif score <= 49 and score >= 30:
    print("D for Don't bother to come back for a resit.")
else:
    print("Be like say you need God ooh.")
    

if gradpt > 5.0:
    print("Invalid score. Out of bounds!")
elif gradpt <= 5.0 and gradpt >= 4.5:
    print(f"Congrats! You got an A with a whopping {gradpt}.")
elif gradpt <= 4.5 and gradpt >= 3.0:
    print(f"You got a B at {gradpt}. Well done.")
elif gradpt <= 3.0 and gradpt >= 2.5:
    print(f"{score}, An average C.")
elif gradpt <= 2.5 and gradpt >= 2.3 :
    print(f"{gradpt}. D for Don't bother to come back for a resit.")
else:
    print("Be like say you need God ooh.")
    '''


name = input("What is your name?>> ")
def marks():

    what = int(input("How many courses are you offering?>> "))
    courses = []
    for i in range(what):
        print()
        course = input("What courses do you offer?")
        courses.append(course)
    print(courses)

    for course in courses:
        print(f"Enter your score for {course}")
        score = int(input(">>> "))

        if score >= 90:
            letter_grade = 'A'
            gradpt = 4.0

        elif score >= 80:
            letter_grade = 'B+'
            gradpt = 3.5

        elif score >= 70:
            letter_grade = 'B'
            gradpt = 3.0

        elif score >= 60:
            letter_grade = 'C'
            gradpt = 2.5
        else:
            letter_grade = 'E'
            gradpt = 2.5

        print(f"{name}, you had a score of {score}% \n on your {course} test with grade {letter_grade} and a G.P. of {gradpt}")

marks()


'''
    score = float(input("What did you score?>> "))

    if score >= 90:
        letter_grade = 'A'
        gradpt = 4.0

    elif score >= 80:
        letter_grade = 'B+'
        gradpt = 3.5

    elif score >= 70:
        letter_grade = 'B'
        gradpt = 3.0

    elif score >= 60:
        letter_grade = 'C'
        gradpt = 2.5
    else:
        letter_grade = 'E'
        gradpt = 2.5

    print(f"{name}, you had a score of {score}% \n on your {course} test with grade {letter_grade} and a G.P. of {gradpt}")
'''

'''
#for i in courses.insert():
what = int(input("How many subjects do you offer?"))
range = what
print("What courses do you offer?")
course = list(input(">>> "*range))
course.append(courses)
#print(i)
print(f"You offer {len(courses)} courses and {course} is one of them.")


'''