#7001ICT Programming Principles, Workshop 4, 2.3 Problem 2
#Program that given an input n, output the firstn Fibonacci numbers on a max of 4 results per row.

#Start Fibonacci variable numbers
previousNumber = 1
nextNumber = 0
swap = 0
fibonacci = []

#Count Lines
counterLine = 0

#Recieve a number from the user to start the loop
number = (int(input("Enter a number: ")))

#Check if the provided number is valid
if number > 0:

    #While loop will run "number" times
    while number > 0:
        #swap will save the next number while we calculate the future next number
        #and then alocate it on the new previous number
        swap = nextNumber
        nextNumber = previousNumber + nextNumber
        previousNumber = swap

        #Save the number on a list
        fibonacci.append(previousNumber)

        #Count the number of interactions per line
        counterLine += 1

        #Decrease the number of interactions on the loop
        number -= 1

        #Check if we already had 4 interactions
        if (counterLine%4) == 0:
            #The * will print the list without parentheses
            print (*fibonacci)

            #Clean the list for the next interactions
            fibonacci.clear()
        
        #If there are less than four interactions and the loop
        # has ended we print the remaining numbers on the list
        elif number == 0:
            print (*fibonacci)
else:
    print ("Invalid number.")

