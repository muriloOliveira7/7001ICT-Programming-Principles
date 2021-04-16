#7001ICT Programming Principles, Workshop 4, 2.4 Problem 3
#Program that given an input number n, print a diamond shape with 2*n-1 rows.

#Recieve a number from the user to start the loop
number = (int(input("Enter a positive number: ")))

#Check if the provided number is valid
if number > 0:
    #Do the top of the dimond
    for i in range(number):
        #Row will be "numbre-1" spaces and "i*2+1" * 
        #first row for number=5 will be 4 spaces (5-1=4) and 1 * (0*2+1=1)
        print(" "*(number-i), "*"*(i*2+1))

    #Do the botton of the dimond starting after the middle row
    for i in range(number-2, -1, -1):
        #On our example set i to start on 3 (number-2)
        #to do the inverse dimond and complete the botton
        print(" "*(number-i), "*"*(i*2+1))
else:
    print("Invalid number")