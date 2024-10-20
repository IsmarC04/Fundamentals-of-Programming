#Assume the days of the week are numbered 0, 1, 2, 3, 4, 5, 6 from Sunday to Saturday. Write a program that asks a day number, and prints the day name (a string).

day_number = int(input("Write a day number:"))

if day_number == 0:
    print("Sunday")
elif day_number == 1:
    print("Monday")
elif day_number == 2:
    print("Tuesday")
elif day_number == 3:
    print("Wednesday")
elif day_number == 4:
    print("Thursday")
elif day_number == 5:
    print("Friday")
elif day_number == 6:
    print("Saturday")
else:
    print("you write invalid number")