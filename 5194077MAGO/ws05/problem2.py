#7001ICT Programming Principles, Workshop 5, 3.3 Problem 2

#Write a function that converts all digits in a string to underline.

#Convert function
def convertNumberToUnderscore (convertString):
    """Convert all numbers in a string to underscore."""
    for i in convertString:
        #Check if the character is a number
        if i.isdigit() == True:
            #Convert the number to underscore
            convertString = convertString.replace(i, "_")
    return convertString
    

#Recieve a string from the user
userString = input("Enter a string: ")

print (convertNumberToUnderscore(userString))