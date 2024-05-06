grades =[[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
average = sum(grades[0])/len(grades[0])
average1 = sum(grades[1])/len(grades[1])
average2 = sum(grades[2])/len(grades[2])
average3 = sum(grades[3])/len(grades[3])
average4 = sum(grades[4])/len(grades[4])
grades = [[average],[average1],[average2],[average3],[average4]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students = sorted(students)
dict(zip(students,grades))
average_grades = dict(zip(students,grades))
print(average_grades)