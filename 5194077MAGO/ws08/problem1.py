#7001ICT Programming Principles, Workshop 8, 3.2 Problem 1

#A function that given a list of numbers, 
#rotate the numbers until it returns to the initial form

def rotate(list):
    """Rotate the numbers until it returns to the initial form"""
    i = 0
    while i < len(list):
        #take the last number on the list and concatenate it
        #with other slice without the last number
        list = (list[-1:]+list[:-1])
        print (list)
        i += 1

#Recieve a list from the user
list1 = [int(item) for item in input("Input a list: ").split()]

rotate(list1)