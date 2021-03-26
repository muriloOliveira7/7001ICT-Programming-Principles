#7001ICT Programming Principles, Workshop 3, 2.2 Problem 2

#Recieve the data from the user
baseprice = float(input("How much is the base price? "))
weight = float(input("What is the weight? "))
distance = float(input("What is the distance? "))

#Calculate discount by the distance
if distance < 250:
    discount = 0
elif 250 <= distance < 500:
    discount = 0.10
elif 500 <= distance < 1000:
    discount = 0.15
elif 1000 <= distance < 2000:
    discount = 0.20
elif 2000 <= distance < 3000:
    discount = 0.35
else:
    discount = 0.50

#Calculate the final cost of the delivery
cost = baseprice * weight * distance * (1 - discount)

print ('\nThe shipping cost is ',cost) 