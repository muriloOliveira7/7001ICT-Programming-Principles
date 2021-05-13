#7001ICT Programming Principles, Workshop 8, 3.5 Problem 4

#A function that concatenate two lists in descending order

def concatDescOrder (list1, list2):
    """Concatenate two lists in descending order"""
    concatList = []
    i = 0
    j = 0

    list1.sort(reverse=True)
    list2.sort(reverse=True)

    while i < (len(list1)) and j < (len(list2)):
        #Check which item is greater and append to the result list
        if list1[i] > list2[j]:
            concatList.append(list1[i])
            i += 1
        elif list2[j] > list1[i]:
            concatList.append(list2[j])
            j += 1
        else:
            concatList.append(list1[i])
            i += 1
        
        #Check if it is the last element of one of the lists
        #If it is the last element we concatenate the rest of the other list
        if i == (len(list1)):
            concatList= concatList + (list2[j:])
            break
        elif j == (len(list2)):
            concatList = concatList + (list1[i:])
            break

    return concatList


#Recieve the first list from the user
list1 = [int(item) for item in input("List 1: ").split()]

while True:
    #Check if the list1 is not empty
    if not list1:
        break
    else:
        #Recieve the second list from the user
        list2 = [int(item) for item in input("List 2: ").split()]

        print (concatDescOrder(list1, list2))

        #Recieve the first list from the user
        list1 = [int(item) for item in input("List 1: ").split()]