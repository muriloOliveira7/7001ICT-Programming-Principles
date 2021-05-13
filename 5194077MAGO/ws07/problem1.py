#7001ICT Programming Principles, Workshop 7, 3.1 Problem 1

#Program that copy all content from a source file to a target one
#without empty lines and print how many lines were deleted

#Recieve files from the user
inputFile = input("Source file name: ")
outputFile = input("Target file name: ")
totalEmptyLines = 0

#Open the files in read mode and "a" - Append - will append to the end of the file
with open(inputFile, 'r') as file_in, open(outputFile, 'a') as file_out:
    for line in file_in:          
        # check if the line is empty, if not, add the line to new file, if it is empty add one to the counter
        if line.strip():
            file_out.write(line)
        else:
            totalEmptyLines += 1

print (totalEmptyLines)