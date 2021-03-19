#7001ICT Programming Principles, Workshop 2, 2.3 Problem 1

#Recieve the data from the user
length = float(input("Length of park (m): "))
width = float(input("Width of park (m): "))
litres = float(input("Litres per square metre: "))

#Print the result of the litres per square metre of the retangle
print ("Litres required = ", (length*width)*litres)