#7001ICT Programming Principles, Workshop 8, 3.4 Problem 3

#Program that counts the words, lines and characrters of a file

def checkArithmeticPogression (list):
    """Check if a list  form  an  arithmetic  progression"""
    #Save the first subtraction
    result = (list[1]-list[0])

    #Start a loop from the third element and compare subtraction with the last result
    for i in range (2,len(list)):
        if result != (list[i]-list[i-1]):
            return False

        #Save the next subtraction
        result = (list[i]-list[i-1])
        i += 1

    #Return true if all intereactions above where sucessful
    return True


#Recieve files from the user
inputFile = input("File name: ")

with open(inputFile, 'r') as file_in:
    #Read each line of the file
    for line in file_in:
        #convert each item of the list to int splited by space
        lineNumbers = [int(item) for item in line.split()]
        print (*lineNumbers, checkArithmeticPogression(lineNumbers))
