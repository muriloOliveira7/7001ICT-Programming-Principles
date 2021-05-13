#7001ICT Programming Principles, Workshop 8, 3.3 Problem 2

#A function that takes two lists as the input arguments and
#returns a list of all the elements in the first list that 
#occur in the second list without duplicate elements.

def checkEqualNumbers (list1, list2):
    """Returns a list of all the elements in the first list that 
    occur in the second list without duplicate elements."""
    equalNumbers = []
    i = 0

    #Remove duplicate elements from list1
    list1 = list(dict.fromkeys(list1))

    #Loop each element of the list1 against all elements on list2
    # to find elements that are equal and add to a result list
    for i in list1:
        for j in list2:
            if i == j:
                equalNumbers.append(i)
                break
    
    return equalNumbers

#Recieve the first list from the user
list1 = [int(item) for item in input("List 1: ").split()]

while True:
    #Check if the list1 is not empty
    if not list1:
        break
    else:
        #Recieve the second list from the user
        list2 = [int(item) for item in input("List 2: ").split()]

        print (checkEqualNumbers(list1,list2))

        list1 = [int(item) for item in input("List 1: ").split()]