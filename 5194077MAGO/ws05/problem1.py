#7001ICT Programming Principles, Workshop 5, 3.2 Problem 1

#Program that prompts for and reads strings until a string starts with 
#“A”is  entered,  then  prints  the  shortest  string  that  was  entere

#Recieve a string from the user
userString = input("Enter a string: ")
shortestString = userString

while userString.startswith("A")!=True:
    userString = input("Enter a string: ")
    if len(userString)<len(shortestString):
        shortestString = userString

#print ("Shortest was:", "'{}'".format(shortestString))
print ("Shortest was:", "'%s'" % shortestString)