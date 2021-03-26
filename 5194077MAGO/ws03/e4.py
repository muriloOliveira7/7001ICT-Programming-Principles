#7001ICT Programming Principles, Workshop 3, 2.4 Problem 4

#Variables
WAGE = 36.25
OVERHOUR = 1.5*WAGE

#Recieve the data from the user
workHours = int(input("How many hours were worked? "))
cars = int(input("Total number of cars sold for the week? "))

if workHours > 37:
    salary = 37*WAGE+(workHours-37)*OVERHOUR
    if cars > 5:
        salary = salary + (cars-5)*200
else:
    salary = workHours*WAGE

print ('The salary is ',salary)
