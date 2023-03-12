
"""
Topic: A calculator function code
def calculator():
    prob = int(input('Would you like to:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Raise to a power\n'))

    if prob == 1:
        a = int(input('Enter the first number: '))
        b = int(input('Enter the second number: '))
        result = a + b
        print(f'{result} is the sum of {a} and {b}.')
    
    elif prob == 2:
        c = int(input('Enter the first number: '))
        d = int(input('Enter the second number: '))
        result = c - d
        print(f'{result} is the difference between {c} and {d}.')

    elif prob == 3:
        e = int(input('Enter the first number: '))
        f = int(input('Enter the second number: '))
        result = e * f
        print(f'{result} is the product of {e} and {f}.')

    elif prob == 4:
        g = int(input('Enter the numerator: '))
        h = int(input('Enter the denominator: '))
        result = g / h
        print(f'{result} is the quotient of {g} and {h}.')

    elif prob == 5:
        y = int(input('Enter the base number: '))
        power = int(input('Enter the exponent: '))
        result = y ** power
        print(f'{result} is the exponential product of {y} raised to the power of {power}.')

    else:
        print('Invalid input. Please try again.')

calculator()
"""
'''''
Topic: A time recording code for business workers
print("Attendance Register: Please ensure you sign in and out while entering and leaving the office.")
print()

import datetime

while True:
    time_stamp = input("Enter 1 to clock in, 2 to clock out, 3 to view hours spent at work and 4 to exit: ")

    now = datetime.datetime.now()

    start_time = now.replace(hour=8, minute=0, second=0, microsecond=0)
    close_time = now.replace(hour=18, minute=0, second=0,microsecond=0)

    if time_stamp == "1":
        if now <= start_time:
            print("Welcome to work! Have a productive day.")
        else:
            print("You are late to work. Expect a query.")
    elif time_stamp == "2":
        if now >= close_time:
            print("Goodbye! I hope you had a productive day.")
        elif now <= close_time and now >= start_time:
            print("You have successfully clocked out.")
        else:
            print("Sorry, you can't clock out. It's not within work hours yet.")
    elif time_stamp == "3":
        if now >= start_time and now <= close_time:
            print(f"You have spent {now - start_time} hours at work today.")
        else:
            print("Sorry, you can't view hours. It's not within work hours yet.")
    elif time_stamp == "4":
        break
    else:
        print("Invalid input.")
        '''''
''''
Topic: Random Stuff that might not work<... feel free...>
courses = []
for i in courses():
    what = int(input("How many subjects do you offer?"))
    range = what
    print(len(range))
 print("What courses do you offer?")
    course = list(input(">>> "*range))
    course.append(courses)
    print(i)
    print(f"You offer {len(courses)} courses and {course} is one of them.")
'''