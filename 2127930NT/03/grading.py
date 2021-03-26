# Write a program that asks the user for a number of marks, and prints the grade awarded

marks = int(input("How many marks? "))

if marks >= 85:
    print("7")
elif marks >= 75:
    print("6")
elif marks >= 60:
    print("5")
elif marks >= 50:
    print("4")
else:
    print("F")
