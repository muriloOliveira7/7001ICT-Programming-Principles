#7001ICT Programming Principles, Workshop 7, 3.3 Problem 3

#Program that recieve a file and print the 
#avarage number of each row of numbers

lineInFile = 0

#Recieve files from the user
inputFile = input("File name: ")

with open(inputFile, 'r') as file_in:
    #Read each line of the file
    for line in file_in:
        lineInFile += 1
        #convert each item of the list to int splited by space
        lineNumbers = [int(item) for item in line.split()]
        print ('The average of line', lineInFile,'is', sum(lineNumbers)/len(lineNumbers))