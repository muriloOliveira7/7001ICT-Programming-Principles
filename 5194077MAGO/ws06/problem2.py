#7001ICT Programming Principles, Workshop 6, 3.2 Problem 2

#Program  that  allows  the  user  to  enter  two  lists  of  
#integers, calculate  thesum of the first and the last integers 
#in each list, and print the larger sum.

totalList = 0

def sumFirstLastList (list):
    """Sum the first and the last number of a list"""

    #Check if the list has more than one element and sum the first and last element
    if len(list)>1:
        totalList = list[0] + list[-1]

    #If the list has only one element it is the total
    else:
        totalList = list[0]
    
    return totalList

#Recieve two lists from the user
list1 = [int(item) for item in input("List 1: ").split()]
list2 = [int(item) for item in input("List 2: ").split()]

#Check if both are not empty
if not list1 or not list2:
    print ("Please enter at least one number in each list.")
else:

    #Check each list has a higher total or if they have the same total
    if sumFirstLastList(list1) > sumFirstLastList(list2):
        print (sumFirstLastList(list1))
    elif sumFirstLastList(list1) == sumFirstLastList(list2):
        print ("Same")
    else:
        print (sumFirstLastList(list2))