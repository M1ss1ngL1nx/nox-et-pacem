'''
from datetime import datetime, timedelta
#import datetime as dt
schedule = {'reception': "11:49", 'office':"11:50", 'HR': "08:15", 'Cleaning': "07:30"}
print(schedule['reception'])

for i,j in schedule.items():
    print(f"All who work in ",i.title()," should be at work by ",j," a.m")

clk_in = datetime.now()

name = input('What is your name?>> ')
current_time = clk_in.strftime("%H:%M")#converts current_time format to hours and minutes
print(f"The time is {current_time}")


occ = input('What sector of this organization are you working in?>> ').lower()

print(clk_in + timedelta(minutes = 50))

if current_time <= schedule[occ]:
    print(f"You are early. You arrived at {current_time}.")
elif current_time > schedule[occ]:
    print("You are late.")
#else:
 #   print("Not an option")
'''
#Functions
#def myfunc(fname):
 #   print(fname + " Kane")
#fname = input("What's your first name?")
#myfunc(fname)
'''
def secfunc(name, pet, nummer):
    print(f"Good day, {name}. Your {pet} is waiting for you in the hotel's shuttle.")
name = input('What is your name?>> ')
que = input('Do you have a pet?> ')

if que == 'yes':
    pet = input('Cat, dog or others?> ')
else:
    print(f'Good day,{name}')

nummer = input('Please enter your phone number- ')
qu = input(f"Is this {nummer} ,your phone number?")
print("Thank you!")
secfunc(name, pet, nummer)
'''
#(add, sub, mult, div, exp,power):
def calculator(add, sub, mult, div, exp,power):
    prob = int(input('Would you like to: 1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Raise exponentially'))
    if prob == 1:
        a = int(input('Enter the first>> '))
        b = int(input('Enter the second>> '))
        add = a + b

        print(f'{a + b}is the sum of {a} and {b}.')

    elif prob == 2:
        c = int(input('Enter the first>> '))
        d = int(input('Enter the second>> '))
        sub = c - d

        print(f'{c-d}is the difference b/n {c} and {d}.')

    elif prob == 3:
        e = int(input('Enter the first>> '))
        f = int(input('Enter the second>> '))
        mult = e * f

        print(f'{mult}is the product of {e} and {f}.')

    elif prob == 4:
        g = int(input('Enter the first>> '))
        h = int(input('Enter the second>> '))
        div = g / h

        print(f'{div}is the product of dividing {g} and {h}.')

    elif prob == 5:
        y = int(input('Enter the number>> '))
        power = int(input('To what power will you be raising it>> '))
        exp = y ** power

        print(f'{exp}is the exponential raise of {y} to the power {power}.')

    else:
        print("Invalid function")

calculator(add, sub, mult, div, exp,power)
