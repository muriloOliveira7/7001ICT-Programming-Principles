#7001ICT Programming Principles, Workshop 4, 2.2 Problem 1
#Program that prints the number of positive numbers that were entered.

#Start our counter variable
positivesNum = 0

#Recieve a number from the user to start the loop
number = (int(input("Enter a number: ")))

#While loop will run until the number 0 is provided
while number != 0:
    #If the number is positive we increment our counter
    if number > 0:
        positivesNum += 1

    #Recieve a new number from the user
    number = (int(input("Enter a number? ")))

print (positivesNum, "positive numbers were entered.")