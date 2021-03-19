##7001ICT Programming Principles, Workshop 2, 2.3 Problem 2

#Recieve the data from the user
bigClassrooms = int(input("How many big classrooms? "))
smallClassrooms = int(input("How many small classrooms? "))
CLASS = 25

#Print the number of classes
print ("Number of classes = ", (bigClassrooms*45+smallClassrooms*22)//25)
