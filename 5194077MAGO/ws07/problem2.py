#7001ICT Programming Principles, Workshop 7, 3.2 Problem 2

#Program that print the first two linesand the last two lines of the file

#Recieve files from the user
inputFile = input("File name: ")

#Open the file and add each line as an element of a list
inputFile = open(inputFile, 'r')
fileText = inputFile.readlines()
inputFile.close()

#Use slice to select the first and last two elements of the list
head = fileText[:2]
tail = fileText[-2:]
print (*head, *tail, sep = "")