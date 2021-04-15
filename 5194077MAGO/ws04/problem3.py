#7001ICT Programming Principles, Workshop 4, 2.4 Problem 3
#Program that given an input number n, print a diamond shape with 2*n-1 rows.

#Recieve a number from the user to start the loop
number = (int(input("Enter a positive number: ")))

if number > 0:
    for i in range(number):
        print(" "*(number-i), "*"*(i*2+1))
    for i in range(number-2, -1, -1):
        print(" "*(number-i), "*"*(i*2+1))
else:
    print("Invalid number")