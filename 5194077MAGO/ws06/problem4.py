#7001ICT Programming Principles, Workshop 5, 3.4 Problem 4

#Program that allows the user to enter the marks of 5 students in 
#4 courses,Output the highest average marks for students and courses. 

import numpy as np

marks = []
students = 5 #number of students
courses = 4 #number of courses
highestAverageStudentMark = 0
highestAverageCourseMark = 0

# Recieve the marks from the user
for i in range(students):
    print ('Student', i+1, '(courses 1-4): ', end = '')
    # recieve a list of intergers from the user splited by spaces
    row = list(map(int, input().split()))
    # add the list above as a row to an array
    marks.append(row)

#Sum the elements in the columns and search the highest one
highestAverageCourseMark = np.amax(np.sum(marks, axis = 0)/students)

#Sum the elements in the rows and search the highest one
highestAverageStudentMark = np.amax(np.sum(marks, axis = 1)/courses)

print(highestAverageStudentMark)
print(highestAverageCourseMark)