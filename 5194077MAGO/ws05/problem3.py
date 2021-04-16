#7001ICT Programming Principles, Workshop 5, 3.4 Problem 3

#function to calculate the number of daysfrom starting year to ending year inclusive

def isLeapYear (year):
    """Return if it is a Leap year or not."""
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def daysInYears (startYear, endYear):
    """Calculate the total number of days between two years."""
    totalDays = 0
    for i in range (startYear, endYear+1):
        #Sum 366 days for leap years and 365 for normal years
        if isLeapYear(i):
            totalDays = totalDays + 366
        else:
            totalDays = totalDays + 365
    return totalDays


#Recieve a number from the user to start the loop
year1 = (int(input("Year 1: ")))
year2 = (int(input("Year 2: ")))

#Check if the input years are valid
if year1 > 0 and year2 > 0:
    if year2 > year1:
        print ("Number of days:", daysInYears(year1, year2))
    else:
        print ("Number of days:", daysInYears(year2, year1))
else:
    print ("Please, enter a valid year")