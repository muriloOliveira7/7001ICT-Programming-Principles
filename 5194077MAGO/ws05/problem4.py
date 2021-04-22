#7001ICT Programming Principles, Workshop 5, 3.5 Problem 4

#Program that repeatedly asks the user for room dimensions until
#either dimensionentered is zero or less. For each room print the 
#length and width (to the nearest millimetre),and the total length 
#of carpet required in whole metres, both lengthwise and widthwise.

import math

roll = 3.66

def totalCarpet (dimension1, dimension2, roll):
    """Calculate lengthways and widthways of a carpet based on two dimensions and width of the roll."""
    length = 0
    width = 0
    
    #Check if the values are valid
    if dimension1 <= 0 or dimension2 <= 0:
        print('Please enter valid numbers for the dimensions')
    
    #Set the length to be the greater dimension
    else:
        if dimension1 > dimension2:
            length = dimension1
            width = dimension2
        else:
            length = dimension2
            width = dimension1
        
        print('Length',length)
        print('Width',width)

        #Calculate and print the lengthways and widthways 
        #based on the dimensions and width of the carpet roll.
        print('Total length required lengthways = ', math.ceil(length*math.ceil(width/3.66)), "m")
        print('Total length required widthways = ', math.ceil(width*math.ceil(length/3.66)), "m")



#Recieve a number from the user to start the loop
dimension1 = (float(input("Enter room dimension 1 (m): ")))
dimension2 = (float(input("Enter room dimension 2 (m): ")))

#While statement will run until both dimensions are "0"
while True:
    if dimension1 == 0:
        if dimension2 == 0:
            break
        else:
            totalCarpet (dimension1,dimension2,roll)
            dimension1 = (float(input("Enter room dimension 1 (m): ")))
            dimension2 = (float(input("Enter room dimension 2 (m): ")))
    else:
        totalCarpet (dimension1,dimension2,roll)
        dimension1 = (float(input("Enter room dimension 1 (m): ")))
        dimension2 = (float(input("Enter room dimension 2 (m): ")))
    

