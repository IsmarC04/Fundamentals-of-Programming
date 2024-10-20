#You go on a wonderful holiday leaving on day number 3 (a Wednesday). You return home after 137 sleeps. Write a general version of the program which asks for the starting day number, and the length of your stay, and it will tell you the name of day of the week you will return on. 
d = 3 #day when you vacation start
s = 137 #length of your vacation
total_days = d + s
n = int(total_days / 7) # "n" represent a number of full weeks which you spend on vacation
r = total_days - 7*n # "r" day when you will return

if r == 0:
    print("Sunday")
elif r == 1:
    print("Monday")
elif r == 2:
    print("Tuesday")
elif r == 3:
    print("Wednesday")
elif r == 4:
    print("Thursday")
elif r == 5:
    print("Friday")
else:
    print("Saturday")