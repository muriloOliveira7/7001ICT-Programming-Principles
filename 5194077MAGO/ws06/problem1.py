#7001ICT Programming Principles, Workshop 6, 3.1 Problem 1

#Program that eads string, convert to lowercase, sort and 
#print the words into descending order lexicographically.

def lowerAndSortString (list):
    """Convert all words to lower case and sort then nto descending order lexicographically"""

    #Convert all elements to lowercase
    for i in range(len(list)):
        list[i] = list[i].lower()
    
    #Sort descending order lexicographically
    print (sorted(list, reverse=True))

#Recieve a list of strings from the user
list = [item for item in input("Enter the list items : ").split()]

while True:
    lowerAndSortString(list)
    list = [item for item in input("Enter the list items : ").split()]

    #Check if the user let the input empty
    if not list:
        break
