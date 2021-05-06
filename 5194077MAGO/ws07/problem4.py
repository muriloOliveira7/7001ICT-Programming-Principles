#7001ICT Programming Principles, Workshop 7, 3.4 Problem 4

#Program that counts the words, lines and characrters of a file

characrtersInFile = 0
wordsInFile = 0
linesInFile = 0

#Recieve files from the user
inputFile = input("File name: ")

with open(inputFile, 'r') as file_in:
    #Read each line of the file
    for line in file_in:
        linesInFile += 1

        #convert the lines to a list of words splited by space
        lineContent = line.split()

        #sum all elements of the list to have the words count
        wordsInFile += len(lineContent)

        #get the lenght of the line to get all characters
        characrtersInFile += len(line)

print (characrtersInFile)
print (wordsInFile)
print (linesInFile)