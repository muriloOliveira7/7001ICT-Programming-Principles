#7001ICT Programming Principles, Workshop 3, 2.3 Problem 3

#Variables
num = []

#Recieve the data from the user
num1 = (int(input("Integer 1? ")))
num2 = (int(input("Integer 2? ")))
num3 = (int(input("Integer 3? ")))

#Easy Way
num.append (num1)
num.append (num2)
num.append (num3)

num.sort(reverse=True)
print ('Sorted:', num)

#Another Way
if num1 > num2 and num1 > num3:
    large = num1
    if num3 > num2:
        medium = num3
        small = num2
    else:
        medium = num2
        small = num3
elif num2 > num1 and num2 > num3:
    large = num2
    if num1 > num3:
        medium = num1
        small = num3
    else:
        medium = num3
        small = num1
elif num3 > num1 and num3 > num2:
    large = num3
    if num1 > num2:
        medium = num1
        small = num2
    else:
        medium = num2
        small = num1
elif num1 == num2 and num1 > num3:
    large = num1
    medium = num2
    small = num3
    if num1 < num3:
        large = num3
        medium = num1
        small = num2
elif num1 == num3 and num1 > num2:
    large = num1
    medium = num3
    small = num2
    if num1 < num2:
        large = num2
        medium = num1
        small = num3
else:
    if num1 > num2:
        large = num1
        medium = num2
        small = num3
    else:
        large = num2
        medium = num3
        small = num1

print ('Sorted: ',large,medium,small)
