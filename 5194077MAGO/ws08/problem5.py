#7001ICT Programming Principles, Workshop 8, 3.6 Problem 5

#A program that reports the names and number of club 
#members infected up to each meeting from a recorded file

def checkBookFever (list,bookFeverList):
    """Check the first infected person or new ones based 
    on a list of infected pesrsons and a record meeting"""
    newInfected = []
    #Check if there is already someone infected
    if not bookFeverList:
        for x in range(len(list)):
            for c in list[x-1]:
                #Check for the simbol for first infected person
                if c == '*':
                    #Append first infected and remove the simbol
                    bookFeverList.append(list[x-1][:-1])
                    #Append individuals next him
                    bookFeverList.append(list[x-2])
                    bookFeverList.append(list[x])
    else:
        for x in range(len(list)):
            for j in range (len(bookFeverList)):
                #Check if the person before him is infected
                #If he is infected add this person a pre-list
                if list[x-1] == bookFeverList [j]:
                    for name in bookFeverList:
                        #Check if the new infected person is not on pre-list or final list
                        if list[x] not in bookFeverList:
                            if list[x] not in newInfected:
                                newInfected.append(list[x])
                #Check if the person is infected
                #If he is add the person before him to the pre-list
                elif list[x] == bookFeverList [j]:
                    for name in bookFeverList:
                        #Check if the new infected person is not on pre-list or final list
                        if list[x-1] not in bookFeverList:
                            if list[x-1] not in newInfected:
                                newInfected.append(list[x-1])

    #Add pre-list to final list
    bookFeverList = bookFeverList + newInfected
    return bookFeverList

lineInFile = 0
bookFeverList = []

#Recieve file from the user
inputFile = input("File name: ")

with open(inputFile, 'r') as file_in:
    #Read each line of the file
    for line in file_in:
        #convert each item of the list to int splited by space
        lineContent = [str(item) for item in line.split()]

        #Save the number of the meeting and delete it from the content
        lineInFile = lineContent[0]
        del lineContent[0]

        bookFeverList = checkBookFever(lineContent,bookFeverList)
        if bookFeverList:
            print (lineInFile, *bookFeverList, len(bookFeverList))