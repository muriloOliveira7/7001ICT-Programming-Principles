#7001ICT Programming Principles, Workshop 3, 2.1 Problem 1

#Recieve the data from the user
mark = float(input("How many marks? "))

if mark >= 85:
    print (7)
elif 85 > mark >= 75:
    print (6)
elif 75 > mark >= 60:
    print (5)
elif 60 > mark >= 50:
    print (4)
else:
    print ('F')