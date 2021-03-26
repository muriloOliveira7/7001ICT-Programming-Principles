# Write program to calculate the weekly wages plus over time plus commission for the car dealer.

hours = int(input("How many hours were worked? "))
cars = int(input("Total number of cars sold for the week? "))
baseRate = 36.25
baseSalary = 37 * baseRate

if hours > 37:
    salary = baseSalary + (hours - 37) * (baseRate * 1.5) # base salary + extra hours * penalty rate
    if cars > 5:
        salary = salary + ((cars - 5) * 200) # salary + commission
else:
    salary = baseSalary

print(f'The salary is {salary}')