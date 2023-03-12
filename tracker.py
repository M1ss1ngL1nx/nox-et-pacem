"""
Create a python file named tracker.py and implement the following instructions below.

********** ATTENDANCE TRACKER **********
Write a program to allow a user implement the following:

Enter 1 to clock in
Enter 2 to clock out
Enter 3 to view hours spent in the office
Enter 4 to exit

You should be able to do the following to your code:
1. Check if a user is early or late to work
2. Check if a user wants to leave the office early
3. Display the time a user has spent in the office

Hint: import datetime module
"""
from datetime import datetime as dt, timedelta
def track():
    clk = dt.now()
    current_time = clk.strftime("%H:%M")
    clk_in = float(input("What time are you clocking in, please?> "))
    if clk <= clk_in:
        print("You have arrived early.")
    elif clk > clk_in:
        print("You have arrived late.")

hrspent = clk_in + timedelta(hours= 1)
print(hrspent)