#Assume you have the assignment numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20] 
#Write a loop that prints each of the numbers on a new line. 
#Write a loop that prints each number and its square on a new line. 
#Write a loop that adds all the numbers from the list into a variable called total. You   should set the total variable to have the value 0 before you start adding them up, and print the value in total after the loop has completed. 
#Print the product of all the numbers in the list. (product means all multiplied together

numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20] 
for number in numbers:
    print(number)

for number in numbers:
    print(number**2)


total = 0
for number in numbers:
    total += number
print(f" total of all number: {total}")

product = 1
for number in numbers:
    product *= number
print(f"Product of all numbers:{product}")