# program to count even numbers and poisitive numbers
list1 = [] # create an empty list to store numbers
list2 = [] # create a list of positive numbers

while True:
    num = input("Enter a number: ") # user enters input of strings
    if num  == "0": # exit the loop
        break
    else:
        list1.append(int(num)) # adding the element to the empty list
# find positive numbers entered
for num in list1: # iterating each number in list
    if num > 0: # checking condition
        list2.append(int(num))

print ("Positive numbers entered: ", len(list2))