#7001ICT Programming Principles, Workshop 3, 2.3 Problem 3

#Recieve the data from the user
num1 = (int(input("Integer 1? ")))
num2 = (int(input("Integer 2? ")))
num3 = (int(input("Integer 3? ")))

#Total of input numbers will be used as the number of interactions
n = 3

#Using Bubble Sort algorithm
while n >=0:
    if num3>num2:
        swap = num2
        num2 = num3
        num3 = swap
    elif num2 > num1:
        swap = num1
        num1 = num2
        num2 = swap
    n -= 1

print (num1, num2, num3)