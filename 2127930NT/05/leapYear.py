# Given starting and ending years, write a function to calculate the number of days

def isLeapYear (year):
    """Function that calculates if leap year"""
    # leap year if it is divisible by 4 AND not divisible by 100 OR divisible by 400
    if year == year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True

def getLeapYear (firstYear, lastYear):
    """Function that prints leap year"""
    for i in range (firstYear, lastYear+1):
        if isLeapYear(i): # call function
            return i

def countDays (firstYear, lastYear):
    """Function that calculates the total number of days between two years."""
    days = 0
    leapYear = 366
    nonleapYear = 365
    # for loop with 2 arguments
    for i in range (firstYear, lastYear+1):
        # pass boolean value function to check condition and count total number of days
        if isLeapYear(i): # call function
            days = days + leapYear
        else:
            days = days + nonleapYear
    return days

# Ask user for input year
year1 = (int(input("Year 1: ")))
year2 = (int(input("Year 2: ")))

print ("Number of days:", countDays(year1, year2)) # call function
print ("Leap year: ", getLeapYear(year1, year2))  # call function - the only leap year is 2000