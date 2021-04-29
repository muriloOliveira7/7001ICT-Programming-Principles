#7001ICT Programming Principles, Workshop 5, 3.3 Problem 3

#Program to find if there are at least two "g" grouped in a string

def findDoubleLetters (userString):
    """Check if all 'g's in the string has other on the side"""

    countPosition = 0
    result='False'

    #Loop through each character of the string
    for i in userString:
        #Check if the string has only one characrter
        if len(userString) == 1:
            result='False'
            print (result)
            break

        #Check if the first character of the string is a g
        elif countPosition == len(userString)-1:
            if i == 'g':
                if userString[countPosition-1] == 'g':
                    result='True'
                    print (result)
                    break
                else:
                    result='False'
                    print (result)
                    break
        
        #Check if the g is in the middle of the string and check each side of it
        elif countPosition > 0:
            if i == 'g':
                if userString[countPosition-1] == 'g' or userString[countPosition+1] == 'g':
                    result='True'
                else:
                    result='False'
                    print (result)
                    break
        
        #If the string has more than one character, but the first character is a 'g'
        #we check the next character
        else:
            if i == 'g':
                if userString[countPosition+1] == 'g':
                    result='True'
                else:
                    result='False'
                    print (result)
                    break
        countPosition = countPosition +1
        if countPosition == len(userString):
            print (result)

#Recieve a string from the user
userString = input("Enter a string: ")

findDoubleLetters(userString)